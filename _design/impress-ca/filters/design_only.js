function(doc, req) {
  return doc._id.slice(0, 8) == "_design/";
}
