function(head, req) {
  var row;
  start({
    "headers": {
      "Content-Type": "text/markdown"
     }
  });
  while(row = getRow()) {
    send(row.doc.slide_content + '\n');
  }
}
