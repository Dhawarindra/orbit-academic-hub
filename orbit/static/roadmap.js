// Keep the draft and operation token available when the save acknowledgement is lost.
document.addEventListener("submit", async (event) => {
  const form = event.target;
  if (form.method !== "post") return;
  event.preventDefault();
  if (form.getAttribute("aria-busy") === "true") return;
  const alert = document.getElementById("save-error");
  alert.hidden = true;
  form.setAttribute("aria-busy", "true");
  try {
    const response = await fetch(form.action, {
      method: "POST",
      body: new FormData(form, event.submitter),
      headers: {Accept: "application/json"},
    });
    if (response.status === 403) throw new Error("Formulir kedaluwarsa. Muat versi terbaru.");
    const result = await response.json();
    if (!response.ok) throw new Error(result.error);
    // Reload once after a same-page save so the new revision and flash are rendered.
    if (new URL(result.location, window.location.href).pathname === window.location.pathname) {
      window.history.replaceState(null, "", result.location);
      window.location.reload();
    } else {
      window.location.assign(result.location);
    }
  } catch (error) {
    alert.querySelector("p").textContent = error instanceof TypeError || error instanceof SyntaxError
      ? "Konfirmasi simpan belum diterima. Input masih tersedia. Coba kirim kembali."
      : error.message;
    alert.hidden = false;
    alert.focus();
  } finally {
    form.removeAttribute("aria-busy");
  }
});
