var gulp = require("gulp")
var cssnano = require("gulp-cssnano")
var rename = require("gulp-rename")
var uglify = require("gulp-uglify");
var bs = require("browser-sync").create()


gulp.task("css",function () {
    gulp.src("./css/*.css")
    .pipe(cssnano())
    .pipe(rename({"suffix":".min"}))
    .pipe(gulp.dest("./css/dist/"))
});
//处理js文件

gulp.task("js",function(){
    gulp.src("./js/*.js")
    .pipe(uglify())
    .pipe(rename({"suffix":".min"}))
    .pipe(gulp.dest("./dist/js/"));
});

// 定义一个处理css文件改动的任务
gulp.task("css",function () {
    gulp.src("./css/*.css")
    .pipe(cssnano())
    .pipe(rename({"suffix":".min"}))
    .pipe(gulp.dest("./css/dist/"))
    .pipe(connect.reload())
});

// 定义一个监听的任务
gulp.task("watch",function () {
    // 监听所有的css文件，然后执行css这个任务
    gulp.watch("./css/*.css",["css"])
});


var sass = require("gulp-sass");
// 处理css的任务
gulp.task("css",function () {
    gulp.src(path.css + "*.scss")
        .pipe(sass().on("error",sass.logError))
        .pipe(cssnano())
        .pipe(rename({"suffix":".min"}))
        .pipe(gulp.dest(path.css_dist))
});


//修改文件自动刷新浏览器
gulp.task("bs",function () {
    bs.init({
        "server": {
            "baseDir": "./"
        }
    });
});

// 定义一个处理css文件改动的任务
gulp.task("css",function () {
    gulp.src("./css/*.css")
    .pipe(cssnano())
    .pipe(rename({"suffix":".min"}))
    .pipe(gulp.dest("./css/dist/"))
    .pipe(bs.stream())
});

// 定义一个监听的任务
gulp.task("watch",function () {
    gulp.watch("./css/*.css",["css"])
});

// 执行gulp server开启服务器
gulp.task("server",["bs","watch"])




//将sass转换为css
var sass = require("gulp-sass");
// 处理css的任务
gulp.task("css7",function () {
    gulp.src("./css/css/*.scss" )
        .pipe(sass().on("error",sass.logError))
        .pipe(cssnano())
        .pipe(rename({"suffix":".min"}))
        .pipe(gulp.dest("./dist/css"))
});
