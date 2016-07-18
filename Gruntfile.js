module.exports = function (grunt) {
    grunt.initConfig({
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
    grunt.loadNpmTasks('grunt-contrib-sass');

    grunt.registerTask('build', [
        'sass'
    ]);
    grunt.registerTask('default', [
        'build'
    ]);
};