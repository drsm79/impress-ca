function(doc){
  if (doc.slide_content){
    emit(doc.slide_number, doc.slide_title)
  }
}
