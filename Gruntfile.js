module.exports = function (grunt) {
    grunt.initConfig({
        concat: {
            options: {
                // change this when minified
                // for now this is to make
                // it readable post-concat
                separator: '\n\n'
            },
            dist: {
                src: [
                    'src/client/js/order.js'
                ],
                dest: 'static/js/bundle.js'
            }
        },

        sass: {
            dist: {
                files: {
                    'static/css/hd.css': 'src/client/scss/hd.scss'
                }
            }
        }
    });

    // below can be run manually and is automatically
    // called on heroku by sticking it into the
    // post-install script in package.json
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-sass');

    grunt.registerTask('build', [
        'concat',
        'sass'
    ]);
    grunt.registerTask('default', [
        'build'
    ]);
};