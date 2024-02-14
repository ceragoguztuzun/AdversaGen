# AdversaGen: Adversarial Tool powered by GPT

## Use of Language Model to Predict Genetic Disease from Phenotypes

### Abstract

Genetic diseases, stemming from mutations at DNA sites called SNPs, manifest in physical characteristics known as phenotypes. These phenotypes can vary widely, from facial traits to persistent symptoms. Exploiting lists of phenotypes and SNPs, an attacker can potentially infer the genetic disease of an individual. This poses serious privacy risks, such as genomic discrimination or blackmail. This paper presents "AdversaGen"©, utilizing OpenAI's ChatGPT to predict diseases from phenotypes with high accuracy. It also explores the application of privacy algorithms like differential privacy to anonymize genomic datasets further.

### Problem Statement

The research aims to leverage OpenAI's ChatGPT to predict genetic diseases based on given phenotypes, assess the accuracy of predictions, and implement Differential Privacy to protect genomic privacy.

### Literature Search

The study reviews existing research, including:
- **De-anonymizing Genomic Databases Using Phenotypic Traits** by E. Ayday et al., highlighting the threat of re-identifying individuals from genomic databases using phenotypic data.
- **PEDIA: Prioritization of Exome Data by Image Analysis** by Tzung-Chien Hsieh et al., which focuses on improving the diagnosis of rare genetic disorders using phenotypic information and AI.
- **Analysis of large-language model versus human performance for genetics questions** by Dat Duong, Benjamin D. Solomon, comparing ChatGPT's performance with humans in answering genetic questions.
- **A Categorical Archive of ChatGPT Failures** by Ali Borji, categorizing ChatGPT failures, providing insights into its limitations.

### Methods

#### AdversaGen Tool Workflow
The workflow includes:
- **Database**: Utilizing XML databases (original "vanilla" and differential privacy-derived "strawberry") containing patient phenotypes and genetic diseases.
- **Pipeline**: Querying ChatGPT with phenotypes, processing responses, generating feedback queries, and predicting diseases using ensemble learning.
- **Prediction**: Using ensemble learning to predict diseases and compare predictions with the original labels.

#### Prompt Generating Pipeline
The pipeline involves:
- Querying ChatGPT with carefully worded prompts to retrieve SNPs associated with phenotypes.
- Iteratively generating feedback queries based on previous responses to infer genetic diseases.

### Datasets

Datasets follow a DTD schema and include:
- **Vanilla Dataset**: Comprising real data from online genomic databases.
- **Strawberry Dataset**: Generated using differential privacy to protect privacy, with randomized mixing of phenotypes and diseases.

### Results

The accuracy of AdversaGen on the "vanilla" dataset ranges from 60-80%. The "strawberry" dataset, with noise introduced by differential privacy, generally exhibits lower accuracy but occasionally surpasses the "vanilla" dataset.

### Analysis

The "strawberry" dataset, despite its noise, occasionally yields higher accuracy due to the random nature of noise. However, its overall accuracy tends to be lower.

### Future Work

Future research should address limitations imposed by API constraints and explore applications of AdversaGen in facial phenotypes for genetic privacy.

### Impact

AdversaGen poses serious privacy risks, allowing attackers to predict genetic diseases with ease. Differential privacy offers a means to mitigate these risks.

### Conclusion

ChatGPT demonstrates potential in replacing specialized ML models for genetic disease prediction. Implementing differential privacy enhances genomic privacy but reduces prediction accuracy.

### Acknowledgments

Acknowledgment to Dr. Erman Ayday for guidance and insights.

### References

- Citations from relevant research papers and resources.

For the Python code of the pipeline, visit the GitHub repository [here](https://github.com/adighosh18/AdversaGen).
