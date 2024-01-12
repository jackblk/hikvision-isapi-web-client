document.querySelectorAll("#form-submit").forEach((elem) => {
  elem.addEventListener("submit", (e) => {
    e.preventDefault();
    console.log(e);
    let authkeyEl = document.getElementById("authkey");
    postData(
      `/door/${e.target.getAttribute("doorId") || 1}`,
      {
        command: e.submitter.getAttribute("cmd"),
      },
      authkeyEl ? authkeyEl.value : ""
    )
      .then((data) => {
        console.log(data);
        let title = "Success";
        if (data?.error) {
          title = "Error";
          document.getElementById("res-toast").className =
            "toast text-bg-warning";
        } else {
          document.getElementById("res-toast").className =
            "toast text-bg-success";
        }
        toast(title, data.message);
      })
      .catch((err) => {
        console.log(err);
        document.getElementById("res-toast").className = "toast text-bg-danger";
        toast("Error", err.message);
      });
  });
});

function toast(title, body) {
  document.getElementById("toast-title").innerText = title;
  document.getElementById("toast-body").innerText = body;
  const toastElem = document.getElementById("res-toast");
  const toast = new bootstrap.Toast(toastElem);
  toast.show();
}

async function postData(url = "", data = {}, authkey = "") {
  // Default options are marked with *
  const response = await fetch(url, {
    method: "POST", // *GET, POST, PUT, DELETE, etc.
    mode: "cors", // no-cors, *cors, same-origin
    cache: "no-cache", // *default, no-cache, reload, force-cache, only-if-cached
    credentials: "same-origin", // include, *same-origin, omit
    headers: {
      "Content-Type": "application/json",
      // 'Content-Type': 'application/x-www-form-urlencoded',
      "X-Auth-Key": authkey,
    },
    redirect: "follow", // manual, *follow, error
    referrerPolicy: "no-referrer", // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data), // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}
