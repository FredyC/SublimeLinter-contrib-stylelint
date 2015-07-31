
var fs = require("fs")
var postcss = require("postcss")
var stylelint = require("stylelint")
var reporter = require("./reporter")

/// css to be processed
var fileName = process.argv[2];
var css = fs.readFileSync(fileName, "utf8");

/// load the .stylelintrc config, if --config has been provided.
var config;
var index = process.argv.indexOf("--config");
if(index > -1){
	config = JSON.parse( fs.readFileSync(process.argv[index+1]) );
}

/// start the linting process.
postcss([
        stylelint( config )
	,reporter()
    ])
    .process(css, {
        from: fileName
    })
    .then()
    .catch(function(err) {
        console.error(err.stack)
    })
