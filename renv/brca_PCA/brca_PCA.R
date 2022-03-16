library(mlbench)
library(factoextra)

# load BRCA dataset
data(BreastCancer)

# remove cases with incomplete data (=NA present in the dataframe)
full_data = BreastCancer[complete.cases(BreastCancer), ]

# remove id and class columns 
data = subset(full_data, select = -c(Class, Id))

# perform PCA with rescaling and centering
pca = princomp(data.matrix(data), cor = TRUE)

# plot projections of data on PCs
png('brca_pcs_R.png')
print(fviz_pca_ind(pca, geom="point", habillage=full_data$Class, palette=c('blue','red')))
dev.off()

