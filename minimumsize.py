import aspose.pdf as ap

compressPdfDocument = ap.Document("electrical assignment 2.pdf")

pdfoptimizeOptions = ap.optimization.OptimizationOptions()

pdfoptimizeOptions.image_compression_options.compress_images = True

pdfoptimizeOptions.image_compression_options.image_quality = 0

compressPdfDocument.optimize_resources(pdfoptimizeOptions)

compressPdfDocument.save("compressing.pdf")