# Impress CouchApp

## [Markdown](http://code.google.com/p/pagedown/) + [Impress](https://github.com/bartaz/impress.js) + [CouchDB](http://couchdb.apache.org)

 * Write markdown
 * Run import script (import_md.py)
 * Push to database
 * Impress your friends

## Use
Invoke the import script with the location of a markdown file to create slide
documents in the $PWD

    python import_md.py $MY_MARKDOWN/$MY_TALK

Push the couchapp and the documents to CouchDB using your favourite couchapp
client.

Once up you can retrieve the markdown via the following list:

    http://localhost:5984/talk/_design/impress-ca/_list/markdown/slides?reduce=false&include_docs=true
