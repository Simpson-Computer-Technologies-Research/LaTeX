<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>


# Integration with U-Substitution and Natural Logarithms
The best way to solve complex logarithms that contain a binomial in both the numerator and denomator of f(x) is to use u-substitution.

### **Question 1:**
Solve the integral below using u-substitution and natural logarithms.
> ‏‏‎ ‎
> $\int \frac{(x+5)}{(x^2+5)}dx$
> ‏‏‎ ‎

### **U-Substitution:**
Set $\mu$ to $(x^2 + 5)$ then solve for $d\mu$
> ‏‏‎ ‎
> $let$ $\mu = (x^2 + 5)$
>
> $let$ $d\mu = \frac{d}{dx}\left[\mu\right]dx$
>
> $\therefore d\mu = \frac{d}{dx}\left[(x^2 + 5)\right]dx$
>
> $\therefore dx = \frac{d\mu}{2x}$
> ‏‏‎ ‎


### **Solve the equation:**
Solve the equation by moving the numerator constants to the front of the integral and using the natural logarithm function (ln) to integrate the remaining variables.
> ‏‏‎ ‎
> = $\int \frac{x+5}{\mu}\frac{d\mu}{2x}$
>
> = $\frac{1}{2}\int \frac{5}{\mu}d\mu$
>
> = $\frac{5}{2}\int \frac{1}{\mu}d\mu$
>
> = $\frac{5}{2}\int \frac{1}{(x^2 +5)}dx$
>
> = $\frac{5}{2}$ $ln(x^2 + 5) + C$
>
> $\therefore$ $\int \frac{(x+5)}{(x^2+5)}dx$ = $\frac{5}{2}$ $ln(x^2 + 5) + C$
> ‏‏‎ ‎