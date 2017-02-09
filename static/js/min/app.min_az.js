 /*!
  * project-name
  * http://example.url/
  * @author Labrin
  * @author-url http://labrin.net/
  * @version 0.1.0
  * @updated 2017-02-06 */
 (function() {
     $(function() {
         return console.log("hello world!")
     })
 }).call(this), $(function() {
     var a = $(window).width();
     a <= 767 && $(".navbar-collapse").find(".btn").removeClass("pull-right"), $(window).scroll(function() {
         $(window).scrollTop() > 700 && $(".top").fadeIn(1e3), $(window).scrollTop() < 700 && $(".top").fadeOut(1e3)
     }), $(".top").click(function() {
         var a = $("body").offset().top;
         $("body").stop().animate({
             scrollTop: a
         }, 2e3)
     }), $(".progress").animate({
         width: "100%"
     }, 2e3, function() {
         "#file" == window.location.hash && $(".btnFile").click(), $("header,section,footer").show(), $(".progress,.logo").hide(), $("html").ready(function() {
             $("#videoblock").vide("/static/video/video.mp4", {
                 volume: 1,
                 playbackRate: 1,
                 muted: !0,
                 loop: !0,
                 autoplay: !0,
                 position: "50% 50%",
                 resizing: !0,
                 bgColor: "transparent",
                 className: "",
                 poster: !1
             })
         });
         var a = [],
             b = $(window).height() / 1.5;
         $(".sectionAnimate").each(function(b, c) {
             var d = $(c).offset().top,
                 e = {
                     sectionIndex: b,
                     sectionOffset: d
                 };
             a.push(e)
         }), $(window).scroll(function() {
             var c = $(this).scrollTop();
             $.each(a, function(a, d) {
                 if (c > d.sectionOffset - b) {
                     var e = $($(".sectionAnimate")[a]),
                         f = e.find(".animated");
                     f.each(function(a, b) {
                         setTimeout(function() {
                             $(b).addClass(function(a) {
                                 return a = $(this).attr("data-direction")
                             })
                         }, 500 * a)
                     })
                 }
             })
         })
     }), $("#filer_input").filer({
         limit: 5,
         maxSize: 2,
         extensions: ["docs", "docx", "pdf", "djvu"],
         showThumbs: !0,
         addMore: !0,
         captions: {
             button: "Fayl yüklə",
             removeConfirmation: "Siz faylı silməyə əminsiniz?",
             errors: {
                 filesLimit: "yalnız {{fi-limit}} fayl yükləmək olar",
                 filesType: "Yalnız doc,docx və pdf format qəbul edilir",
                 filesSize: "{{fi-name}} çox böyük fayldır! zəhmət olmasa {{fi-maxSize}} MB dan az həcmli fayl yükləyin.",
                 folderUpload: "fayl yüklənir"
             }
         },
         afterShow: function() {
             $(':input[type="submit"]').removeClass('disabled');
             $(':input[type="submit"]').prop('disabled', !1)
         },
         onRemove: function() {
             if ($('.jFiler-item').length === 1) {
                 $(':input[type="submit"]').addClass('disabled');
                 $(':input[type="submit"]').prop('disabled', !0)
             }
         }
     }), $(".jFiler-input-button").addClass("font-open-s-b"),
     $('.student').change(function() {
        if($(this).val() == '1') {
            $('#univercity').removeClass('hide');
        }
        else {
            $('#univercity').addClass('hide');
        }
    })
 })