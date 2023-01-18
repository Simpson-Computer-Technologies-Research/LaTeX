<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script type="text/x-mathjax-config">
  MathJax.Hub.Config({ tex2jax: {inlineMath: [['$', '$']]}, messageStyle: "none" });
</script>

# Integration with U-Substitution and Natural Logarithms
We can solve a complex integral that contains a binomial in the denominator of $f(x)$ using u-substitution.

### **Question 1:**
Solve the integral below using u-substitution and natural logarithms.
> ‏‏‎ ‎
> $\int \frac{5x}{(x^2+5)}dx$
> ‏‏‎ ‎

### **Prepare the U-Substitution:**
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
Solve the equation by dividing 5x by 2x then moving the resulting $\frac{5}{2}$ to the front of the integral. Then, use the natural logarithm function (ln) to integrate the remaining variables.
> ‏‏‎ ‎
> = $\int \frac{5x}{\mu}\frac{d\mu}{2x}$
>
> = $\frac{5}{2}\int \frac{1}{\mu}d\mu$
>
> = $\frac{5}{2}ln(\mu) + c$
>
> = $\frac{5}{2}ln(x^2 + 5) + c$
>
> $\therefore$ $\int \frac{5x}{(x^2+5)}dx = \frac{5}{2}ln(x^2 + 5) + c$
> ‏‏‎ ‎

<br><br>


# **Integrals for Mr.N**
## **Question 1: Easy**
> ‏‏‎ ‎
> Solve with Integration by Parts:
> 
> $\int x^2cos(3x)dx$
> ‏‏‎ ‎

## **Question 2: Medium**
> ‏‏‎ ‎
> Solve by completing the square:
> 
> $\int \frac{(x + 4)}{(x^2 + 2x + 5)}dx$
> ‏‏‎ ‎

## **Question 3: Hard**
> ‏‏‎ ‎
> Solve with Feynman's Technique:
> 
> $\int_0^\infty \frac{\sin x}{x}dx$
> ‏‏‎ ‎





# **Notes**
## **Derivation**
The derivation of a function is defined as $f(x)\prime$
> ‏‏‎ ‎
> $f(x)\prime = \frac{d}{dx}[f(x)]$
> ‏‏‎ ‎

The derivation of the natural logarithm function is as follows:
> ‏‏‎ ‎
> $\frac{d}{dx}ln(\mu) = \frac{\mu\prime}{\mu}$
> ‏‏‎ ‎

## **Natural Logarithms and Integrals**
The natural logarithm function is denoted by the symbol $ln$ and is defined as follows:
> ‏‏‎ ‎
> $\int \frac{1}{\mu} = \frac{ln(\mu)}{\mu\prime} + c$
> ‏‏‎ ‎