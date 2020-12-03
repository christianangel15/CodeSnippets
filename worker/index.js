async function handleRequest(request) {
  const url = "https://static-links-page.signalnerve.workers.dev/static/html"
  const data = [{ "name": "Link Name", "url": "https://linkurl" },
  { "name": "Link Name", "url": "https://linkurl" },
  { "name": "Link Name", "url": "https://linkurl" }
  ]
  const init = {
    headers: {
      "content-type": "text/html;charset=UTF-8",
    },
  }
  const jsn = JSON.stringify(data, null, 2)
  const response = await fetch(url, init)
  if (request.url === "http://localhost:8787/links") {
    return new Response(jsn, {
      headers: {
        "content-type": "application/json;charset=UTF-8"
      }
    })
  }
  else {
    return response
  }

}

addEventListener("fetch", event => {
  return event.respondWith(handleRequest(event.request))
})