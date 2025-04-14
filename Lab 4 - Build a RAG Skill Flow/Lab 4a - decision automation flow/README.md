# Using Decision Automation Flow

## Objective

Another integral part of watsonx orchestrate is automating workflow. Besides that, we can also leverage the embedded Generative AI and decision components within the Projects section and insert it into a workflow (or just run as a single skill). 

For this lab, we will be creating an automation workflow which will allow us to set some conditions to place order. The conditions can be for example if an order meets the minimum order requirement or budget requirement. Different condition will result in different results.

## Prepare the zip file

For the purpose of this workshop, you will be uploading a copy of a pre-fabricated object. 

1. Download the project file from here and save to your desktop.
2. If you are using a shared instance, we will need to ensure our project name does not clash with one another.
3. Navigate to your desktop, unzip the file and rename the file to [YourName]_Reorder_automation.
4. Zip up the file again after you’ve renamed.


### * If you are using Macbook, run these steps to rezip the folder:

1. Launch Terminal
2. Go to directory where your folder is located
3. Run command below
```code
zip -r [YourName]_Reorder_automation.zip [YourName]_Reorder_automation
```

## Create a project

1. Return to Watsonx Orchestrate. Click on the Projects tab.
2. From the menu, select Skill studio.
3. In the Skill studio page, click Create, and select Project.
4. Select Import automation and select the zip file which you’ve processed in the first section [YourName]_Reorder_automation.zip and click import

