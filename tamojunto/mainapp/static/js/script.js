const testimonials = document.getElementById('testimonials');
    const pagination = document.getElementById('pagination').children;
    const prevButton = document.getElementById('prev');
    const nextButton = document.getElementById('next');
    let currentIndex = 0;
    let testimonialCount = testimonials.children.length;
    
    function showTestimonial(index) {
      const testimonialWidth = testimonials.children[0].clientWidth;
      testimonials.style.transform = `translateX(${-index * testimonialWidth}px)`;
      Array.from(pagination).forEach(dot => dot.classList.remove('active'));
      pagination[index].classList.add('active');
    }
    
    function nextTestimonial() {
      currentIndex = (currentIndex + 1) % testimonialCount;
      showTestimonial(currentIndex);
    }
    
    function prevTestimonial() {
      currentIndex = (currentIndex - 1 + testimonialCount) % testimonialCount;
      showTestimonial(currentIndex);
    }

    Array.from(pagination).forEach((dot, index) => {
      dot.addEventListener('click', () => {
        currentIndex = index;
        showTestimonial(index);
      });
    });

    nextButton.addEventListener('click', nextTestimonial);
    prevButton.addEventListener('click', prevTestimonial);
    
    showTestimonial(currentIndex);
    
    //setInterval(nextTestimonial, 5000); // Change testimonial every 5 seconds

    //Tela de cadastro membro 

   

  