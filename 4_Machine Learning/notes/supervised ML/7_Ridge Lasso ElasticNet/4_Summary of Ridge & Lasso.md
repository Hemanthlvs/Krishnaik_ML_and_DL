**Relationship between lambda (λ) and coefficients (θ) in Ridge and Lasso regression:**

- In **Ridge regression**, as λ increases, coefficients shrink but never become exactly zero. This helps reduce overfitting by keeping all features but with smaller impact.

- In **Lasso regression**, as λ increases, some coefficients become exactly zero, effectively removing those features. This helps both reduce overfitting and perform feature selection.


# When to Use Ridge, Lasso, and Elastic Net Regression

- **Ridge Regression**  
  Use Ridge when:  
  - You want to reduce overfitting  
  - All features are likely important  
  - There is multicollinearity (features are highly correlated)  
  - You want to keep all features but shrink their coefficients

- **Lasso Regression**  
  Use Lasso when:  
  - You want to perform feature selection (automatically remove unimportant features)  
  - You have many features and expect some to be irrelevant  
  - You want a simpler, more interpretable model with fewer features

- **Elastic Net Regression**  
  Use Elastic Net when:  
  - You want to reduce overfitting **and** perform feature selection simultaneously  
  - You have many features and multicollinearity among them  
  - You want a balance between Ridge and Lasso benefits
