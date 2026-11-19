CREATE TABLE curriculum_snapshot (
    curriculum_id TEXT PRIMARY KEY, program TEXT NOT NULL, version TEXT NOT NULL,
    applicability TEXT NOT NULL, source TEXT NOT NULL, rule_version TEXT NOT NULL,
    content_hash TEXT NOT NULL, status TEXT NOT NULL CHECK(status IN ('active','superseded')),
    UNIQUE(program,version)
);
CREATE UNIQUE INDEX selected_catalog ON curriculum_snapshot(status) WHERE status='active';
CREATE TABLE course (course_id TEXT PRIMARY KEY);
CREATE TABLE curriculum_course (
    curriculum_id TEXT NOT NULL REFERENCES curriculum_snapshot, course_id TEXT NOT NULL REFERENCES course,
    label TEXT NOT NULL, sks INTEGER NOT NULL CHECK(typeof(sks)='integer' AND sks>0),
    category TEXT, source_ref TEXT NOT NULL, rule_version TEXT NOT NULL,
    recommended_sequence INTEGER CHECK(recommended_sequence>=1), prerequisite TEXT NOT NULL, availability TEXT NOT NULL,
    PRIMARY KEY(curriculum_id,course_id)
);
CREATE TABLE offering_binding (
    offering_id TEXT PRIMARY KEY REFERENCES offering, curriculum_id TEXT NOT NULL, course_id TEXT NOT NULL,
    FOREIGN KEY(curriculum_id,course_id) REFERENCES curriculum_course(curriculum_id,course_id)
);
