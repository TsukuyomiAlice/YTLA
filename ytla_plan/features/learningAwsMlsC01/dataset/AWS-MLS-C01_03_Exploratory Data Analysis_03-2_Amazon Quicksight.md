#### Amazon Quicksight:
  * BI/analytics serverless ML service used to build interactive visualizations (dashboards, graphs, charts and reports), perform ad-hoc analysis without paying for integrations of data and leaving the data uncanned for exploration
  * Integrates with sources both in and out of AWS (RDS)
  * In memory computation using Spice Engine
    * Data sets are imported into SPICE
      * Super-fast, Parallel, In-memory Calculation Engine
      * Uses columnar storage, in-memory, machine code generation
      * Accelerates interactive queries on large datasets
    * Each user gets 10GB/month of SPICE (ceiling of 200 GB in Enterprise)
    * Highly available / durable
    * Scales to hundreds of thousands of users
  * Can share analysis (if published) or the dashboard (read only) with users or groups
  * Available as an application anytime on any device (browsers [mobile])
  * Data Sources
    * Redshift
    * Aurora / RDS
    * Athena
    * EC2-hosted databases
    * Files (S3 or on-premises)
      * Excel
      * CSV, TSV
      * Common or extended log format
      * If another file type (eg: json), a conversion is necessary or a feed from Athena (in this case ideally Orc or Parquet for performance efficiency)
    * AWS loT Analytics
    * Data preparation allows limited ETL
  * Quicksight Paginated Reports
    * Reports designed to be printed
    * May span many pages
    * Can be based on existing Quicksight dashboards
  * Q
    * Machine learning-powered
    * Answers business questions with NLP eg: "What are the top-selling items in Florida?"
    * Offered as an add-on for given regions
    * Personal training on how to use it is required
    * Must set up topics associated with datasets
      * Datasets and their fields must be NLP-friendly
      * How to handle dates must be defined
  * Security:
    * Column-Level security (CLS)
    * Multi-factor authentication on your account
    * VPC connectivity
      * Add QuickSight's IP address range to your database security groups
    * Row-level security
      * Column-level security too (CLS) - Enterprise edition only
    * Private VPC access (for on-prem access)
      * Elastic Network Interface, AWS DirectConnect
  * User Management
    * Users defined via IAM, or email signup
    * SAML-based single sign-on
    * Active Directory integration (Enterprise Edition)
    * MFA
  * Pricing
    * Annual subscription
      * Standard: $9 / user /month
      * Enterprise: $18 / user / month
      * Enterprise with Q: $28 / user / month
    * Extra SPICE capacity (beyond 10GB), otherwise more $
      * $0.25 (standard) $0.38 (enterprise) / GB / month
    * Month to month
      * Standard: $12 / user / month
      * Enterprise: $24 / user / month
      * Enterprise with Q: $34 / user / month
    * Additional charges for paginated reports, alerts & anomaly detection, Q capacity, readers, and reader session capacity.
    * Enterprise edition
      * Encryption at rest
      * Microsoft Active Directory integration
      * CLS
  * Use Cases:
    * Interactive ad-hoc exploration / visualization of data
    * Dashboards and KPIs
    * Analyze / visualize data from:
      * Logs in S3
      * On-premise databases
      * AWS (RDS, Redshift, Athena, S3)
      * SaaS applications, such as Salesforce
      * Any JDBC/ODBC data source
  * ML insights feature (only ML capabilties of Quicksight)
    * Anomaly detection (uses Random Cut Forest)
    * Forecasting to get rid of anomalies to make forecast (uses Random Cut Forest)
    * Autonarratives to build rich dashboards with embedded narratives
  * Anti-Patterns
    * Highly formatted canned reports
      * QuickSight is for ad hoc queries, analysis, and visualization
      * No longer true with paginated reports!
    * ETL
      * Use Glue instead, although QuickSight can do some transformations

##### Quicksight Visual Types
  * AutoGraph - automatically selects chart based on input features to best display the data and relationships.  Not 100% effective and might require intervention
  * Bar Charts
    * For comparison and distribution (histograms)
  * Line graphs
    * For changes/trends over time
    * \[stacked] area line charts - allows visualization of different components added up to a change/trend
  * Scatter plots, heat maps
    * For correlation
    * Residual plot \[a type of scatter plot, containining a regression line, measuring how data point(s) overestimating/underestimating target value(s)]
  * Pie graphs, tree maps - Heirarchical Aggregation chart (eg: npm package map)
    * For aggregation
  * Pivot tables
    * For tabular data to aggregate in certain ways into other tables
    * applying statistical functions applied to (multi-dimensional) data  
  * KPIs - chart detailing measurement(s) between current value(s) vs target(s)
  * Geospatial Charts (maps) - map with sized circles annotating certain amounts in certain areas
  * Donut Charts - when precision isn't important and few items in the dimension; show percentile/proportion of the total amount
  * Gauge Charts - compare values in a measure (eg: fuel left in a tank)
  * Word Clouds - word or phrase frequency within a corpus