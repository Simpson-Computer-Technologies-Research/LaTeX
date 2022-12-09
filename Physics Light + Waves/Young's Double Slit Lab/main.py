from ratex import *

# // Build new tex file
r: Build = Build("main.tex", __file__)
r.new(
    title="Young's Double Slit Lab",
    author="Tristan, Ibrahim, Oliver, Aaliya",
    packages = [
        Packages.multirow,
        Packages.changepage,
        Packages.graphicx,
        Packages.fleqn_amsmath,
        Packages.amssymb
    ]
)

# // Purpose
r.add_header("Purpose")
r.add_text(content=r"""
    The purpose of this lab was to measure the wave length ($\lambda$) of a projected laser travelling through a slit then calculate the error percentage produced by our result.
""")

# // Materials
r.add_header("Materials")
r.add_list(type="itemize", items=[
    r.raw_text(r"\textbf{One} Slit"),
    r.raw_text(r"\textbf{One} Line of Measuring Tape"),
    r.raw_text(r"\textbf{One} Red Laser"),
    r.raw_text(r"\textbf{One} Projector"),
    r.raw_text(r"\textbf{Two} Rulers"),
    r.raw_text(r"\textbf{One} Piece of Paper")
])

# // Procedure
r.add_header("Procedure")
r.add_list(type="enumerate", items=[
    r.raw_text(r"The sheet of paper was taped to the black-board."),
    r.raw_text(r"The laser was positioned infront of the slit, both facing the piece of paper on the black-board."),
    r.raw_text(r"Using a pencil, the blocks made by the laser and slit were marked on the piece of paper."),
    r.raw_text(r"The distance between the middles of two of the blocks made by the slits was measured. ($\Delta x$)"),
    r.raw_text(r"The distance from the slit to the black-board was measured. ($L$)"),
    r.raw_text(r"The width of the slits double line was measured using the projector, two rulers, and the slit itself. ($d$)")
])

# // Observations
r.add_header("Observations")
r.add_text(r"The observations below exhibit the distance from the split to the black board ($L$) and the distance from the middles of two blocks projected by the laser travelling through our provided slit. ($\Delta x$)")
r.add_list(items=[
    r.raw_text(r"$L$ $\approx$ $73cm$ $\approx$ $7.3$ $\times 10^{-1}$ $m$"),
    r.raw_text(r"$\Delta x$ $\approx$ $0.7cm$ $\approx$ $7.0\times 10^{-3}$ $m$")
])

# // Calculations
r.add_header(r'Caclulations: Solve for $d$')
r.add_text(r"Before solving for $\lambda$, we must find $d$ (the width of the slit). To do this we used a projector (magnifier) and the formula below.\newline\newline")
r.add_eq(r"\therefore d = \frac{(1mm)(slit width on projection)}{(1mm on projection)} = \frac{(1mm)(3.2mm)}{(6.1mm)} \approx 5.24\times 10^{-4}m")
r.add_newline(1)

# // Calculations 
r.add_header(r'Calculations: Solve for $\lambda$')
r.add_text(r"After finding $d$ we can solve for $\lambda$ using the formula shown below and substitute in our already found variables and givens into the equation.\newline\newline")
r.add_eq(r"\therefore \lambda = \frac{\Delta xd}{L} = \frac{(7.0\times 10^{-3})(5.24\times 10^{-4})}{(7.3\times 10^{-1})} \approx 5.02 \times 10^{-6}m")
r.add_newline(1)

# // Calculations
r.add_header(r"Calculations: Error Percentage")
r.add_text(r"After solving for an experimental result, we use the standard formula to calculate the error percentage.")
r.add_eq(r"\therefore Error \% = \left(\frac{Experimental - Theoretical}{Theoretical}\right) \times 100")
r.add_eq(r"\therefore Error \% = \left(\frac{(5.02 \times 10^{-6}) - (6.53 \times 10^{-9})}{(6.53 \times 10^{-9})}\right) \times 100 \approx 7.6\times 10^5\;\%")

# // Source of Errors
r.add_header("Sources of Errors")
r.add_list(type="enumerate", items=[
    r.raw_text(r"The blocks produced by the laser travelling through the slit were too close together. This made measuring the distances far harder and far more inaccurate."),
    r.raw_text(r"Measuring from the projector can produce inaccurate results. Because of how large and pixelated the projection is, achieving accurate measurements can be difficult."),
    r.raw_text(r"The laser was too far away / close to the the slit.")
])

# // Solutions to Errors
r.add_header("Solutions to Errors")
r.add_list(type="enumerate", items=[
    r.raw_text(r"Move to a larger space so we can station the items accordingly."),
    r.raw_text(r"Use a higher resolution projector or have multiple group members measure values then use the average of the results."),
    r.raw_text(r"Measure an appropriate distance for the laser away from the slit.")
])

# // Conclusion
r.add_header("Conclusion")
r.add_text(r"Therefore, by the conclusion of this lab, it was determined that the wave length ($\lambda$) of a laser travelling through a slit was approximately $5.02\;\times 10^{-6}m$ though because of the experimental errors noted above, this result had produced a high error percentage of approximately $7.6\times 10^5\;\%$")

# // Experiment Images
r.add_header("Pictures")
r.add_text(r"The image below is the result of the laser travelling through our provided slit. As you can see, the blocks created by the laser and slit were very close together which made achieving accurate measurements far more difficult.\newline\newline")
r.add_image(path="/images/laser_split.png", scale=0.15)


# // Finalize the build
r.done()