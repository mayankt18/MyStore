$('#slider1, #slider2, #slider3,.owl-carousel').owlCarousel({
    loop: true,
    margin: 20,
    responsiveClass: true,
    responsive: {
        0: {
            items: 1,
            nav: false,
            autoplay: true,
            autoplayTimeout:3000,
            autoplayHoverPause: true,
        },
        600: {
            items: 3,
            nav: true,
            autoplay: true,
            autoplayTimeout:3000,
            autoplayHoverPause: true,
        },
        1000: {
            items: 4,
            nav: true,
            loop: true,
            autoplay: true,
            autoplayTimeout:3000,
            autoplayHoverPause: true,
        }
    }
})
