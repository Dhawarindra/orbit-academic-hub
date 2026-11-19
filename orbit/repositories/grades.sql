-- Grade Rescue subset of ARCH-02. Catalog and profile relations arrive with their modules.
CREATE TABLE workspace (
    singleton INTEGER PRIMARY KEY CHECK(singleton=1),
    owner_scope TEXT NOT NULL UNIQUE, epoch TEXT NOT NULL UNIQUE,
    state_revision INTEGER NOT NULL DEFAULT 0, source_revision INTEGER NOT NULL DEFAULT 0,
    schema_version INTEGER NOT NULL DEFAULT 1
);
CREATE TABLE academic_term (
    term_id TEXT PRIMARY KEY, label TEXT NOT NULL UNIQUE, sequence_no INTEGER NOT NULL UNIQUE
);
CREATE TABLE offering (
    offering_id TEXT PRIMARY KEY, owner_scope TEXT NOT NULL REFERENCES workspace(owner_scope),
    term_id TEXT NOT NULL REFERENCES academic_term, personal_label TEXT NOT NULL,
    class_label TEXT NOT NULL, source TEXT NOT NULL
);
CREATE TABLE enrollment (
    enrollment_id TEXT PRIMARY KEY, offering_id TEXT NOT NULL UNIQUE REFERENCES offering,
    owner_scope TEXT NOT NULL REFERENCES workspace(owner_scope), attempt_no INTEGER NOT NULL DEFAULT 1,
    attempt_key TEXT NOT NULL UNIQUE, status TEXT NOT NULL DEFAULT 'active', source TEXT NOT NULL
);
CREATE TABLE grade_policy (
    policy_id TEXT PRIMARY KEY, offering_id TEXT NOT NULL UNIQUE REFERENCES offering,
    version TEXT NOT NULL, thresholds TEXT NOT NULL, source TEXT NOT NULL
);
CREATE TABLE brp_version (
    brp_id TEXT PRIMARY KEY, enrollment_id TEXT NOT NULL REFERENCES enrollment,
    version_no INTEGER NOT NULL, status TEXT NOT NULL, locked INTEGER NOT NULL DEFAULT 0,
    source TEXT NOT NULL, rule_version TEXT NOT NULL, unsupported_rules TEXT NOT NULL DEFAULT '[]',
    UNIQUE(enrollment_id, version_no)
);
CREATE UNIQUE INDEX active_brp ON brp_version(enrollment_id) WHERE status='active';
CREATE TABLE assessment_node (
    node_id TEXT PRIMARY KEY, brp_id TEXT NOT NULL REFERENCES brp_version,
    parent_id TEXT, kind TEXT NOT NULL, label TEXT NOT NULL, weight_bp INTEGER NOT NULL CHECK(weight_bp BETWEEN 0 AND 10000),
    max_score TEXT, granularity TEXT, position INTEGER NOT NULL,
    UNIQUE(brp_id,node_id), FOREIGN KEY(brp_id,parent_id) REFERENCES assessment_node(brp_id,node_id)
);
CREATE UNIQUE INDEX brp_root ON assessment_node(brp_id) WHERE parent_id IS NULL;
CREATE TABLE assessment_score (
    node_id TEXT PRIMARY KEY REFERENCES assessment_node, earned TEXT, source TEXT NOT NULL, saved_revision INTEGER NOT NULL
);
CREATE TABLE course_target (
    enrollment_id TEXT PRIMARY KEY REFERENCES enrollment, numeric_target TEXT, letter_target TEXT,
    policy_id TEXT REFERENCES grade_policy, source TEXT NOT NULL, saved_revision INTEGER NOT NULL,
    CHECK((numeric_target IS NULL) != (letter_target IS NULL))
);
CREATE TABLE actual_final_revision (
    final_revision_id TEXT PRIMARY KEY, enrollment_id TEXT NOT NULL REFERENCES enrollment,
    revision_no INTEGER NOT NULL, supersedes_id TEXT UNIQUE REFERENCES actual_final_revision,
    numeric_value TEXT, letter_value TEXT, policy_id TEXT REFERENCES grade_policy, outcome TEXT NOT NULL,
    source TEXT NOT NULL, correction_reason TEXT, committed_revision INTEGER NOT NULL,
    occurred_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, UNIQUE(enrollment_id, revision_no)
);
CREATE TABLE scenario (
    singleton INTEGER PRIMARY KEY CHECK(singleton=1), scenario_id TEXT NOT NULL UNIQUE,
    owner_scope TEXT NOT NULL UNIQUE REFERENCES workspace(owner_scope), base_epoch TEXT NOT NULL,
    base_source_revision INTEGER NOT NULL, scenario_revision INTEGER NOT NULL,
    score_overlay TEXT NOT NULL, plan TEXT NOT NULL DEFAULT '{}', target_overlay TEXT NOT NULL DEFAULT '{}',
    assumptions TEXT NOT NULL DEFAULT '{}'
);
CREATE TABLE operation_receipt (
    epoch TEXT NOT NULL, operation_id TEXT NOT NULL, request_hash TEXT NOT NULL,
    result TEXT NOT NULL, committed_state_revision INTEGER NOT NULL, PRIMARY KEY(epoch,operation_id)
);
CREATE TABLE change_log (
    event_id TEXT PRIMARY KEY, epoch TEXT NOT NULL, owner_scope TEXT NOT NULL,
    state_revision INTEGER NOT NULL, source_revision INTEGER NOT NULL, entity_id TEXT NOT NULL,
    event_type TEXT NOT NULL, occurred_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP, UNIQUE(epoch,state_revision)
);
