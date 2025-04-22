<img width="1395" alt="image" src="https://github.com/user-attachments/assets/0e33709c-21d8-4c63-b22a-30f759c79daf" /># Using Decision Automation Flow

## Objective

Another integral part of watsonx orchestrate is automating workflow. Besides that, we can also leverage the embedded Generative AI and decision components within the Projects section and insert it into a workflow (or just run as a single skill). 

For this lab, we will be creating an automation workflow which will allow us to set some conditions to place order. The conditions can be for example if an order meets the minimum order requirement or budget requirement. Different condition will result in different results.

## Create project

1. Go to Skill Studio from left bar

<img width="257" alt="image" src="https://github.com/user-attachments/assets/9ea5fd10-917e-45a0-9ef6-6626cd00d108" />

2. Create Project

<img width="210" alt="image" src="https://github.com/user-attachments/assets/44695055-dd10-4aa7-b425-f6a22ec633d6" />

3. Set your project name to [Your Name]_Reorder_Automation then click Create button

<img width="1599" alt="image" src="https://github.com/user-attachments/assets/967a4faa-7f80-4e57-b0ac-b27c944f72bc" />

## Create workflow

1. Click Workflow

<img width="302" alt="image" src="https://github.com/user-attachments/assets/c76d8bc9-6741-4ca3-94f8-eb350f295a49" />

2. Set your workflowname to [Your Name]_Reorder_Decision_Demo and click Create button

<img width="838" alt="image" src="https://github.com/user-attachments/assets/4341b453-4fa5-4dba-9c63-bfeff1953892" />

## Create variables

1. Click Variables tab and click Create variable button
<img width="1728" alt="image" src="https://github.com/user-attachments/assets/18d4a9b1-e0be-45e4-a508-36453cd5d908" />

2. Set Name to "ReorderQty", Data Type to "Number", and Input to "Yes"
<img width="1402" alt="image" src="https://github.com/user-attachments/assets/37e1dc7a-98b9-4f3a-8cc2-48de86b89ca8" />

3. Reperform same process on step 2 until you get all variables as image below:

<img width="1411" alt="image" src="https://github.com/user-attachments/assets/25f4d2c9-c99c-4bad-a798-d8b06861b5a9" />

## Create decision

1. Go back to Diagram tab -> hover your mouse to Activity -> click Delete icon

<img width="495" alt="image" src="https://github.com/user-attachments/assets/4a77e0cd-f51f-4b72-859b-cc3bf9445492" />

2. Hover your mouse to line between Start and End node -> click + icon

<img width="189" alt="image" src="https://github.com/user-attachments/assets/9f14f3d9-eea9-4edc-a46d-fdf50ffac563" />

3. Select Decision

<img width="738" alt="image" src="https://github.com/user-attachments/assets/1887a6b4-66c5-4ca3-81ef-322d2f4a3311" />

4. Set category to Decision Flow -> set Name to "Get Reorder Qty" -> click Create button

<img width="834" alt="image" src="https://github.com/user-attachments/assets/14acc7ed-5988-4868-96ec-4b28869e6ae6" />

5. Hover your mouse to Decision node -> click Add input icon

<img width="269" alt="image" src="https://github.com/user-attachments/assets/eb71673e-8719-4393-89d4-7e17c1e0a5b0" />

6. Click first input node -> set Name to "ReorderQty" -> set Output type to "Number" -> click second input node -> set Name to UnitPrice -> set Output type to "Number" -> you can see the correct output as image below:

<img width="1063" alt="image" src="https://github.com/user-attachments/assets/863e10ff-d4d5-4dd6-bec5-76ec9c484e15" />

7. Click Decision node -> set Node name to "ReorderValue" -> set Object type to "Number"

<img width="1073" alt="image" src="https://github.com/user-attachments/assets/9aa48e6f-ba23-4b16-9137-a9ed84fe79a7" />

8. Click Decision node -> go to Logic tab -> click + icon in right section -> select Default rule

<img width="1052" alt="image" src="https://github.com/user-attachments/assets/227d2b0c-6e60-4b5e-9013-a29a50ce7694" />

9. Set Name to "SetReorderValue' -> and fill logic box to ```set decision to ReorderQty * UnitPrice ;```

<img width="1395" alt="image" src="https://github.com/user-attachments/assets/569de487-9114-4b72-b2ae-f03c3c06b892" />

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

