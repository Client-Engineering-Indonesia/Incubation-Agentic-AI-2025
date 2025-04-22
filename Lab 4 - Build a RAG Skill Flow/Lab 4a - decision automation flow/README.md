<img width="823" alt="image" src="https://github.com/user-attachments/assets/834c1ded-f58c-4962-9fc8-105227d0f1af" /><img width="903" alt="image" src="https://github.com/user-attachments/assets/95e65e8e-ceab-4934-8828-b75bc688198b" /><img width="1395" alt="image" src="https://github.com/user-attachments/assets/0e33709c-21d8-4c63-b22a-30f759c79daf" /># Using Decision Automation Flow

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

<img width="1407" alt="image" src="https://github.com/user-attachments/assets/7fe75f4e-a41d-4b9e-a39f-87cb24981e08" />

## Create decision

1. Go back to Diagram tab -> hover your mouse to Activity -> click Delete icon

<img width="495" alt="image" src="https://github.com/user-attachments/assets/4a77e0cd-f51f-4b72-859b-cc3bf9445492" />

2. Hover your mouse to line between Start and End node -> click + icon

<img width="189" alt="image" src="https://github.com/user-attachments/assets/9f14f3d9-eea9-4edc-a46d-fdf50ffac563" />

3. Select Decision

<img width="738" alt="image" src="https://github.com/user-attachments/assets/1887a6b4-66c5-4ca3-81ef-322d2f4a3311" />

4. Set category to Decision Flow -> set Name to "[Your Name]_Get_Reorder_Qty" -> click Create button

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

10. Go back to your workflow -> click [Your Name]_Get_Reorder_Qty Node -> click Define data mapping button

<img width="1332" alt="image" src="https://github.com/user-attachments/assets/75c8ada4-51af-47cc-b97d-a1fe64f8a900" />

11. Hover your mouse to first text field -> click <img width="56" alt="image" src="https://github.com/user-attachments/assets/d3033cbe-9c64-43fe-a726-f65c30cc69d9" /> icon

<img width="1211" alt="image" src="https://github.com/user-attachments/assets/b91790ca-a1a7-45dc-b16c-66dd587da026" />

12. Select ReorderQty

<img width="410" alt="image" src="https://github.com/user-attachments/assets/27ba25f7-62fd-47a5-847b-74f3e16024ac" />

13. Repeat same process until your view will be look like image below:

<img width="1239" alt="image" src="https://github.com/user-attachments/assets/91cf6e8c-603e-496a-ac47-a629aebab308" />

14. Go to Output mapping tab -> repeat same process until your view will be look like image below -> click OK button

<img width="1247" alt="image" src="https://github.com/user-attachments/assets/fb0a88fe-d905-48c1-9f61-2f7b243de2ee" />

## Create branch

1. Hover your mouse to line between [Your Name]_Get_Reorder_Qty decision and End node -> click + button -> select Branch

<img width="712" alt="image" src="https://github.com/user-attachments/assets/99805868-fc39-4b6b-a358-95889f97cbb0" />

2. From Branch properties set Name to "CheckMinOrder" -> set Type to Conditional (single) -> set first Path Name to "MinOrderMet" -> leave second Path Name to "Else"

<img width="1330" alt="image" src="https://github.com/user-attachments/assets/15ede59d-a5cc-45a4-997e-826fc5a227cb" />

3. Click Edit conditions button <img width="145" alt="image" src="https://github.com/user-attachments/assets/a2813934-105c-4c07-85e2-bd734a124750" /> -> Select variable to ReorderValue -> set condition to "Greater than or equal to" -> set value to 2000 -> click Save button

<img width="1598" alt="image" src="https://github.com/user-attachments/assets/8ea0123c-f233-4a9b-bd17-27d525a1d6c3" />

## Create rejection message

1. Hover your mouse to line that belongs to Else path -> click + button -> select Generative AI

<img width="806" alt="image" src="https://github.com/user-attachments/assets/a42de4d0-f10f-49be-9ce0-518bc785b13d" />

2. Set Name to "No Min Order Notification" -> click Create button

<img width="832" alt="image" src="https://github.com/user-attachments/assets/759cef76-6e03-45d0-8bde-d46ca131df29" />

3. Fill Context to ```Anda adalah asisten untuk tim pengadaan perusahaan untuk memberikan pesan kepada pengguna sesuai dengan keterangan yang diberikan``` -> add prompt variable named "jumlah_order" and set default value to 1000 -> set Max generated tokens to 500 -> set Prompt input to ```Berikan pesan penolakan karena jumlah_order tidak sesuai dengan kebijakan perusahaan. Kebijakan perusahaan mengatur bahwa jumlah minimum order adalah sebesar 2000. jumlah_order: {{jumlah_order}} ``` -> you can click Generate button to see sample response

<img width="1400" alt="image" src="https://github.com/user-attachments/assets/8c9b07a2-6286-478d-9d6d-13e611a08d43" />

4. Go back to your workflow -> click No Min Order notification node -> click Define data mapping button <img width="300" alt="image" src="https://github.com/user-attachments/assets/4d3ff7cf-987a-4f7f-b94d-e8538e76f6ad" /> -> map jumlah_order variable with ReorderValue

<img width="1226" alt="image" src="https://github.com/user-attachments/assets/c718ec29-eff2-4ae1-b8cf-d8eb796f9cb5" />

5. Go to Output mapping tab -> set generated_text to NoMinOrderMsg -> click OK button

<img width="1232" alt="image" src="https://github.com/user-attachments/assets/2941e7ac-4f4f-46b8-8b56-f5697c44851c" />


## Create salesforce order from skillset 

1. Hover your mouse to line after CheckMinOrder branch -> click + button -> select Assignment

<img width="768" alt="image" src="https://github.com/user-attachments/assets/5c9a6b5a-80b1-4830-8b23-c962560aa399" />

2. Set Name to "Assign Variables" -> click Define data assignments button <img width="314" alt="image" src="https://github.com/user-attachments/assets/5a486c65-89d8-455a-898f-ba8a700ccb74" />

<img width="1177" alt="image" src="https://github.com/user-attachments/assets/6007a8f9-571a-4f92-a0f6-2ef1cb771a3f" />

3. Click Add variable button -> select "PriceBookId" and "AccountId" -> set PriceBookId to "01uIU00000AWG47YAH" -> set AccountId to "001IU00002qLOFFYA4" -> click OK button

<img width="1577" alt="image" src="https://github.com/user-attachments/assets/0527efbe-be8f-424c-8565-91e925d58dc7" />

4. Hover your mouse to line after Assign variables node -> click + button -> select Skill from catalog

<img width="683" alt="image" src="https://github.com/user-attachments/assets/5a8102c0-7af4-4a8f-9df8-bbaf546b42f8" />

5. Type "salesforce" in search field -> select "Salesforce Custom Skills Version2"

<img width="1590" alt="image" src="https://github.com/user-attachments/assets/53c3d845-013c-4218-98fe-afbd9eb4936c" />

6. Click "Create a new order in Salesforce" -> click Save button

<img width="1582" alt="image" src="https://github.com/user-attachments/assets/a8a8a848-eebd-4ccc-9acf-b1644af94949" />

7. Click Define data mapping button <img width="304" alt="image" src="https://github.com/user-attachments/assets/5d2ca666-2e62-4ea0-bb57-48e50bf52d49" /> -> set all Input mapping as image below

<img width="1234" alt="image" src="https://github.com/user-attachments/assets/259456de-ee09-4a9f-b332-1c7374390302" />

8. Go to Output mapping tab -> set all variables as image below

<img width="1238" alt="image" src="https://github.com/user-attachments/assets/2824e0b8-d8b2-485c-a493-65765f3f8c48" />

9. Hover your mouse to line after "Create a new order in salesforce" node -> click + button -> select Skill from catalog

<img width="903" alt="image" src="https://github.com/user-attachments/assets/d0f020c6-34fc-4473-832e-ec033488a862" />

10. Repeat step 5 -> click "Create an order item in salesforce" -> click Save button

<img width="1575" alt="image" src="https://github.com/user-attachments/assets/c86fc39f-58eb-46c0-be3d-84f4bf71c6c1" />

11. Click Define data mapping button <img width="305" alt="image" src="https://github.com/user-attachments/assets/faf05ae9-180e-4f84-ab6a-cb8f93f1a2fe" /> -> Set variables under Input mapping tab as image below

<img width="1231" alt="image" src="https://github.com/user-attachments/assets/4a93dbc3-9e4b-4ebc-a45c-f31c0b7e4be7" />

12. Go to Output mapping tab -> set variables here as image below

<img width="1234" alt="image" src="https://github.com/user-attachments/assets/29710d18-27c3-4bd6-8220-2d22d0f3820f" />

## Create success message

1. Hover your mouse to line before End node -> click + button -> select Generative AI

<img width="927" alt="image" src="https://github.com/user-attachments/assets/490b1e94-7170-4134-adfb-70804b6acc72" />

2. Select Create a Generative AI

<img width="257" alt="image" src="https://github.com/user-attachments/assets/d3377c93-1225-465d-8d4a-bad66396165b" />

3. Set Name to "Order is Success Notification" -> click Create button

<img width="817" alt="image" src="https://github.com/user-attachments/assets/f0c01947-7844-4955-894d-72106d0334e9" />

4. Set Context to ```Anda adalah asisten untuk tim pengadaan perusahaan untuk memberikan pesan kepada pengguna sesuai dengan keterangan yang diberikan``` -> add prompt variables named "order_id", "jumlah_order", "unit_price", and "order_value" -> set Prompt input to ```Berikan pesan keberhasilan karena telah order telah berhasil dibuat pada sistem salesforce. Beritahukan juga order_id jumlah_order, unit_price dan order_value yang dibuat. order_id: {{order_id}}; jumlah_order: {{jumlah_order}}; unit_price (dalam rupiah): {{unit_price}}; order_value (dalam rupiah): {{order_value}}``` -> set Max generated tokens to 500 -> change model to "mistralai/mixtral-8x7b-instruct-v01" -> click Generate button to test the prompt

<img width="1405" alt="image" src="https://github.com/user-attachments/assets/81423307-189e-4094-860c-4594411f3b22" />

5. Click Define data mapping button -> set variables under Input mapping tab as image below

<img width="1238" alt="image" src="https://github.com/user-attachments/assets/2982311f-b119-40af-b223-e365d23ad368" />

6. Go to Output mapping tab -> set all variables to image as below

<img width="1233" alt="image" src="https://github.com/user-attachments/assets/cfa5ca80-612c-4856-bd9c-406fcf3b4096" />

## Publish workflow

1. Click Eye icon <img width="27" alt="image" src="https://github.com/user-attachments/assets/9c2bd472-f8a0-4f18-9560-423c4a8a4a33" /> for each skill in left pane to change access to public

<img width="319" alt="image" src="https://github.com/user-attachments/assets/62fd1918-b091-4738-9d75-151dbac4eb3e" />

2. Click Publish button <img width="100" alt="image" src="https://github.com/user-attachments/assets/9f25e44d-5786-4a3e-b806-523dd9fa12b2" /> -> set Name to "v1.0" -> click Create version publish button

<img width="823" alt="image" src="https://github.com/user-attachments/assets/7e7bd6a0-4000-4ead-a62d-dd378c558c50" />

3. Go to Skill catalog -> type "[Your Name]_Reorder_Automation" in search field -> select item with workflow icon <img width="50" alt="image" src="https://github.com/user-attachments/assets/f1b99eaf-8c22-45af-b7fe-a02e863280d0" />

<img width="1728" alt="image" src="https://github.com/user-attachments/assets/20521ba5-5420-481d-b8bd-b5d8dc33d9bf" />

4. Click Add skill

<img width="334" alt="image" src="https://github.com/user-attachments/assets/dc9525d2-8ec5-486c-99cd-dba8dd60d465" />

5. Go to AI agent configuration -> click Apps and skills -> type "[Your Name]_Reorder_Automation" to find your workflow -> select item with workflow icon <img width="52" alt="image" src="https://github.com/user-attachments/assets/445127aa-8816-4300-add6-147257f5da72" />

<img width="1649" alt="image" src="https://github.com/user-attachments/assets/5a8ec1c8-1867-4694-8aca-c82db4c41407" />

6. Click Add to chat

<img width="264" alt="image" src="https://github.com/user-attachments/assets/77518e61-64fd-4fd7-b286-1af82a7eda54" />

7. Set description to ```Skill is used when user want to perform reorder automation``` to Desciption field -> click Save button

<img width="463" alt="image" src="https://github.com/user-attachments/assets/bbee7f1d-5358-43ab-83ee-849a1f64ac9b" />

8. Now you can run your workflow directly from chat

<img width="1461" alt="image" src="https://github.com/user-attachments/assets/329380f0-0848-4ab6-97af-4ef695d90fe1" />

