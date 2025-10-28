document.addEventListener("DOMContentLoaded", () => {
    document.querySelectorAll("time.utc").forEach(el => {
      const utcString = el.getAttribute("datetime");
      if (!utcString) return;

      const utcDate = new Date(utcString);
      const options = {
        day: '2-digit',
        month: 'short',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        hour12: true
      };
      el.textContent = utcDate.toLocaleString(undefined, options);
    });
  });
