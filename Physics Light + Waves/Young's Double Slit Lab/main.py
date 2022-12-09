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
    The purpose of this lab was to measure the wave length ($\lambda$) of a laser travelling through a slit, then calculate the error percentage produced by our result.
""")

# // Materials
r.add_header("Materials")
r.add_list(type="itemize", items=[
    r.text(r"\textbf{One} Slit"),
    r.text(r"\textbf{One} Line of Measuring Tape"),
    r.text(r"\textbf{One} Red Laser"),
    r.text(r"\textbf{One} Projector"),
    r.text(r"\textbf{Two} Rulers"),
    r.text(r"\textbf{One} Piece of Paper")
])

# // Procedure
r.add_header("Procedure")
r.add_list(type="enumerate", items=[
    r.text(r"The sheet of paper was taped to the black-board."),
    r.text(r"The laser was positioned infront of the slit, both facing the piece of paper on the black-board."),
    r.text(r"Using a pencil, the blocks made by the laser and slit were marked on the piece of paper."),
    r.text(r"The distance between the middles of two blocks made by the laser and slit was measured. ($\Delta x$)"),
    r.text(r"The distance from the slit to the black-board was measured. ($L$)"),
    r.text(r"The width of the slits' double-line was measured using the projector, two rulers, and the slit itself. ($d$)")
])

# // Observations
r.add_header("Observations")
r.add_text(r"During our experiment, our group made the following observations. Below exhibits the distance from the slit to the black-board ($L$) and the distance from the middles of two blocks projected by the laser travelling through our slit. ($\Delta x$)")
r.add_list(items=[
    r.text(r"$L$ $\approx$ $73cm$ $\approx$ $7.3$ $\times 10^{-1}$ $m$"),
    r.text(r"$\Delta x$ $\approx$ $0.7cm$ $\approx$ $7.0\times 10^{-3}$ $m$")
])

# // Calculations
r.add_header(r'Caclulations: Solve for $d$')
r.add_text(r"Before solving for $\lambda$, we must find $d$ (the width of the slit). To do this we used a projector (magnifier) and the formula below.\newline\newline")
r.add_eq(r"\therefore d = \frac{(1mm)(slit width on projection)}{(1mm on projection)} = \frac{(1mm)(3.2mm)}{(6.1mm)} \approx 5.24\times 10^{-4}m")
r.add_newline(1)

# // Calculations 
r.add_header(r'Calculations: Solve for $\lambda$')
r.add_text(r"After finding $d$ we can solve for $\lambda$ by substituting our previous variables into the following equation.\newline\newline")
r.add_eq(r"\therefore \lambda = \frac{\Delta xd}{L} = \frac{(7.0\times 10^{-3})(5.24\times 10^{-4})}{(7.3\times 10^{-1})} \approx 5.02 \times 10^{-6}m")
r.add_newline(1)

# // Calculations
r.add_header(r"Calculations: Error Percentage")
r.add_text(r"After solving for our experimental result, we use the error percentage formula to find how accurate our results really were.")
r.add_eq(r"\therefore Error \% = \left(\frac{Experimental - Theoretical}{Theoretical}\right) \times 100")
r.add_eq(r"\therefore Error \% = \left(\frac{(5.02 \times 10^{-6}) - (6.53 \times 10^{-9})}{(6.53 \times 10^{-9})}\right) \times 100 \approx 7.6\times 10^5\;\%")

# // Source of Errors
r.add_header("Sources of Errors")
r.add_list(type="enumerate", items=[
    r.text(r"The blocks projected by the laser travelling through the slit were too close together. This made measuring the distances far harder and far more inaccurate."),
    r.text(r"Measuring from the projector made achieving accurate results far more difficult due to how large and pixelated the projection is."),
    r.text(r"The laser was too far away / too close to the the slit.")
])

# // Solutions to Errors
r.add_header("Solutions to Errors")
r.add_list(type="enumerate", items=[
    r.text(r"Move to a larger space so we can station the materials accordingly."),
    r.text(r"Use a higher resolution projector or have each of our group members measure values then calculate the average of the results."),
    r.text(r"Measure an appropriate distance for the laser away from the slit.")
])

# // Conclusion
r.add_header("Conclusion")
r.add_text(r"Therefore, upon the conclusion of this lab it was determined that the wave length ($\lambda$) of a laser travelling through a slit was approximately $5.02\;\times 10^{-6}m$ though because of the experimental errors documented above, this result produced a high error percentage of approximately $7.6\times 10^5\;\%$")

# // Experiment Images
r.add_header("Pictures")
r.add_text(r"The image below is the result of the laser travelling through our provided slit. The blocks being projected by the laser and slit were very close together and fuzzy. This was one of the prime sources of errors that was documented above.\newline\newline")
r.add_image(path="/images/laser_split.png", scale=0.15)


# // Finalize the build
r.done()