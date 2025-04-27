# Objective

Now that we have all the skills and workflows in place, we can create a complete flow. You can create this flow within project or skill flow. Since Skill Flow is more readily available, we will build this final flow in the Skill Flows section.

## Create workflow to get supplier and publish it

1. Go to Skill studio -> click Create button -> select Project

![image](https://github.com/user-attachments/assets/9eefe188-1993-42a4-9081-4fbd26f6ba3f)

2. Set Name to [Your name]_Get_Supplier_Flow -> click Create button

![image](https://github.com/user-attachments/assets/14ac6848-10f9-4fc3-b5a1-97bdb2ffbf96)

3. Select Workflow ![image](https://github.com/user-attachments/assets/c5a77d6a-1dce-4cb8-a0ec-4d963e3343d1) -> set Name to [Your name]_Get_Supplier_Flow -> click Create button

![image](https://github.com/user-attachments/assets/0934b78f-b3c6-4d7d-ac6e-ce6dc9218a65)

4. Click Actiity node -> click Delete icon

![image](https://github.com/user-attachments/assets/fbf65de2-d8da-426a-aa31-8d619085f9cc)

5. Go to Variables tab -> create required variables and its details as image below:

![image](https://github.com/user-attachments/assets/24babecc-f319-4e7d-b63c-3c0cde11ad84)

6. Go back to Diagram tab -> hover your mouse to center line -> click + button -> select Skill from catalog

![image](https://github.com/user-attachments/assets/751155a9-363b-4881-8977-a05f6d2ce6cf)

7. Go back to Diagram tab ->  "riset" in search field -> select Riset Supplier

![image](https://github.com/user-attachments/assets/a546dcb8-b243-4ba8-a4f7-d22a83faef61)

8. Select Riset Supplier -> click Save button

![image](https://github.com/user-attachments/assets/a8285ab9-92b0-4689-8f2c-e30e1cf33a82)

9. Click [Your Name]_Get_Supplier_Flow node -> click Define data mapping button ![image](https://github.com/user-attachments/assets/d304fac3-1cd9-4d5d-b2a1-2d9abcee51b3) -> set all variables as image below

![image](https://github.com/user-attachments/assets/9ca9fe86-cfa2-47fc-bbbc-150120dfea78)

10. Go to Output mapping -> set variables as image below -> click OK button

![image](https://github.com/user-attachments/assets/6f39fadd-3724-40d6-a36c-7525f31adce2)

11. Hover your mouse to line before End node -> click + button -> select Generative AI

![image](https://github.com/user-attachments/assets/aaab2402-ce72-4f95-a34a-543dcfee8e7b)

12. Set Name to [Your name]_Best_Supplier Name -> click Create button

![image](https://github.com/user-attachments/assets/e522b507-ec0d-4147-ad4d-0a647f104c2b)

13. Set Context to ```Anda adalah asisten untuk tim pengadaan yang bertugas mencari entitas berdasarkan prompt user. Contoh Prompt: Temukan nama produk berdasarkan pertanyaan yang diberikan user. Pertanyaan User: Berapa stok produk Batik Bali di gudang saat ini? Output: Batik Bali``` -> add prompt variabled named "query" -> set Max generated token to 500 -> change model to mistralai/mixtrail-8x7b-instruct-v01 -> set Prompt input to ```Temukan nama produk berdasarkan pertanyaan yang diberikan user. Berikan jawaban tanpa mengikutkan kata "produk". Pertanyaan User: {{query}}```

![image](https://github.com/user-attachments/assets/9d75fc2a-e4a2-4620-ac8e-9f54b11f1808)

14. Click [Your name]_Get_Product_Name node -> click Define data mapping button ![image](https://github.com/user-attachments/assets/ea8baa3f-a6f4-4864-9b37-10d2e83bb48f) -> map variables under Input mapping tab as image below:

![image](https://github.com/user-attachments/assets/3f591dc0-2559-4275-80e9-34edc64889f3)


15. Set variables under Output mapping tab -> click OK button

![image](https://github.com/user-attachments/assets/46912d42-1c96-4422-9dc2-f2f6793a48d1)


![image](https://github.com/user-attachments/assets/48274b64-ebdb-4965-ac54-83290a6ab482)

14. Go to your previous workflow -> click Define data mapping button ![image](https://github.com/user-attachments/assets/aa31174d-7ec2-4f02-8ce7-0fef44dbd79c) -> map variables under Input mapping tab as image below

![image](https://github.com/user-attachments/assets/30c404a6-9916-494d-9c1b-d3795e202341)

15. Go to Output mapping tab -> set variable as image below -> click OK button

![image](https://github.com/user-attachments/assets/6bbfb4c6-199c-4352-9cf9-941cde7c4d71)

16. Hover your mouse to line before End node -> click + button -> select Generative AI

![image](https://github.com/user-attachments/assets/cbc3e563-f16a-4fc3-bfa9-9aeef390f231)

17. Select Craete a Generative AI ![image](https://github.com/user-attachments/assets/e246831a-8675-41b0-b05e-cb9f7806fe38) -> set Name to [Your name]_Get_Product_Name

![image](https://github.com/user-attachments/assets/a8e5f299-94f2-4b56-861e-a832b9664169)

18. Set Context to ```Anda adalah asisten untuk tim pengadaan yang memberikan jawaban sesuai dengan prompt user``` -> add prompt variabled named "research" -> set Max generated token to 500 -> change model to mistralai/mixtrail-8x7b-instruct-v01 -> set Prompt input to ```Berikan satu nama supplier terbaik berdasarkan hasil riset di bawah ini. Hanya berikan nama supplier saja tidak perlu diberikan penjelasan. Hasil Riset: {{research}}```

16. Ensure you have set visibility of your workflow to Public

![image](https://github.com/user-attachments/assets/91ddfa4c-7599-4b29-b14d-ab3f3a4a67d7)

17. Click Publish button ![image](https://github.com/user-attachments/assets/e4354400-5652-496b-9fab-5a317164e40a) -> set Name to "test-version-01" -> click Create version and publish button

![image](https://github.com/user-attachments/assets/ca06cd6b-4d42-4e93-a085-0a90d8ef8c5e)

## Create skillflow to compile skills

1. Go to Skill catalog by clicking Hamburger icon in top-left side ![image](https://github.com/user-attachments/assets/61b3ce6e-f132-40d5-842d-9ac8d175ea86) -> type "[Your name]_Get_Supplier_Flow" -> select the workflow you have created in previous section

![image](https://github.com/user-attachments/assets/472e0842-6209-4453-915a-25caba640b1d)

2. Click Add skill -> ensure the status has changed to "Added"

![image](https://github.com/user-attachments/assets/53a8bcc9-d14d-4302-8fdc-d0eeb3b03bbf)

3. Go to Skill studio by clicking Hamburger icon in top-left side ![image](https://github.com/user-attachments/assets/61b3ce6e-f132-40d5-842d-9ac8d175ea86) -> click Create button -> select Skillflow

![image](https://github.com/user-attachments/assets/6a9a36ac-d6bf-4563-bdff-47358d49b6c9)

4. Click pencil icon ![image](https://github.com/user-attachments/assets/8621b61d-fdda-41d5-86f0-055d0025be27) in top-left -> set Name to [Your name]_Reorder_Skillflow -> click Save button

![image](https://github.com/user-attachments/assets/04b43b28-0159-4288-abdb-9f3ed04a21cf)

## Add "Research Agent" skill

1. Click + button between Start and End node -> select Custom Form

![image](https://github.com/user-attachments/assets/92dcb981-286d-4468-94f7-d142c63d4141)

2. Click Add skill inside Input Form skill

![image](https://github.com/user-attachments/assets/5798ed23-8b24-4021-a28f-e557f8ad9789)

3. Click + button under Input form that you have created previously -> type "[Your name]_Get_Supplier_Flow" -> click it

![image](https://github.com/user-attachments/assets/4488f34c-8647-4c81-a565-fd1638c60359)

4. Click Add skill

![image](https://github.com/user-attachments/assets/a1ade749-cfc0-4775-83ba-49ecb4c1676a)

5. Click + button under new node -> add Input form as you did in step 5-6 -> your flow will be look like image below

![image](https://github.com/user-attachments/assets/2b5dff09-d94a-49be-9969-146c7873690f)

6. Click first Input form -> click Add input field button ![image](https://github.com/user-attachments/assets/dcd614eb-390b-464b-8743-65b36bb9d013) -> select Paragraph text -> click Next button

![image](https://github.com/user-attachments/assets/7fdb4c60-706f-4d7b-a7b2-906549a5f7c5)

7. Set Display label to "Query" -> click Apply button

![image](https://github.com/user-attachments/assets/85dbd61b-7fea-4894-939d-2839e33fc28f)

8. Set Form title to ```Halo, apa yang bisa saya bantu?``` -> your view will be look like image below

![image](https://github.com/user-attachments/assets/6a0ff13c-e05f-4936-8fed-90b919267e52)

9. Click [Your name]_Get_Supplier_Flow -> click Query field -> click Input form ![image](https://github.com/user-attachments/assets/b115cb59-24df-4901-be83-bb380f00d951) from right page -> click Query

![image](https://github.com/user-attachments/assets/bb7afc28-6d17-4b2a-9e63-1878f6348f47)

10. Please remember that this workflow will generate variable named "SupplierName" as you defined in previous section. You can ensure it by clicking Output tab

![image](https://github.com/user-attachments/assets/34bcd6c6-1f9c-4043-9618-3748b6076188)

11. Set Form name to "Research Result" -> select Single line text  -> click Next button

![image](https://github.com/user-attachments/assets/f18e28f4-3a31-41cf-b46a-bcbf59fa9745)

12. Set Display Name to "Supplier Name" -> click Appply button

![image](https://github.com/user-attachments/assets/839a2c7d-6e22-4b2d-a0e3-18c3a46ca060)

13. Click "Supplier Name" field -> click [Your name]_Get_Supplier_Flow ![image](https://github.com/user-attachments/assets/83ab72d3-fd5e-4cf5-b406-a8c8172897ff) -> click SupplierName ![image](https://github.com/user-attachments/assets/f8836965-c1fd-4dfc-b397-5e0e2cb284bc) -> Ensure you have same view as image below

![image](https://github.com/user-attachments/assets/c3260b12-eb91-4462-9bb3-5a4958d02117)

## Add Salesforce skill

1. Click + button before End node -> click Custom Form -> click Add skill in Input form skill

![image](https://github.com/user-attachments/assets/9d248911-aa03-44fd-b9f9-9eecf38d44b4)  --> ![image](https://github.com/user-attachments/assets/43cec7d2-f43f-4cc2-8915-b3120d81fd52)

2. Set Form title to ```Here is the best supplier of product you query``` -> Add input fields named "Product Name", "Supplier Name", "Order Date", "Reorder Quantity", "Order Status" which are outputs of workflow named "[Your name]_Get_Supplier_Flow" that you have created previously -> map their value as image below: 

![image](https://github.com/user-attachments/assets/ee5d05dd-42a2-4ad1-8155-a9f0858594e7)

### Data type

```code
Product Name = Single line text
Supplier Name = Single line text
Order Date = Date
Reorder Quantity = Decimal
Order Status = Single line text
```

3. Click + button before End node -> select Salesforce ![image](https://github.com/user-attachments/assets/b4374025-b007-43f7-abc4-ba5c80e8a1aa) from opened right pane -> click Add skill in Get all accounts skill

![image](https://github.com/user-attachments/assets/945820d9-d9ec-4a8d-aff2-0a141a4e2369)

4. Click that new node -> click # 1 filterable input -> select Account Name -> set Operator to "is" -> click Value -> map it with [2nd Input Form].[Supplier Name] -> ensure your view look same as image below

![image](https://github.com/user-attachments/assets/6d459867-27ce-4b4f-b85d-75efd838aacd)

5. Click + button before End node -> select Salesforce ![image](https://github.com/user-attachments/assets/b4374025-b007-43f7-abc4-ba5c80e8a1aa) from opened right pane -> click Add skill in Get all price book skill

![image](https://github.com/user-attachments/assets/d22f05ee-5b59-4e75-88ec-dd137fcf7d7b)

6. Click + button before End node -> select Salesforce ![image](https://github.com/user-attachments/assets/b4374025-b007-43f7-abc4-ba5c80e8a1aa) from opened right pane -> click Add skill in Get all products skill

![image](https://github.com/user-attachments/assets/44ba1c7d-a544-4996-a712-76860d8f19ed)

7. Click Get all price book node -> set # 1 Filterable input to "Pricebook Name" -> set Operation to "is" -> map it with [2nd Input Form].[Supplier Name] -> ensure your view look same as image below

![image](https://github.com/user-attachments/assets/1ffd1bb8-6516-41b0-a662-1839d261cc1f)

8. Click Get all products node -> set # 1 Filterable input to "Product Name" -> set Operation to "is" -> map it with [2nd Input Form].[Product Name] -> ensure your view look same as image below

![image](https://github.com/user-attachments/assets/607b210a-f78a-4e0c-b2c4-cc94ed5a4fa9)

## Add "Reorder Automation" skill

1. Click + button before End node -> type "[Your name]_Reorder_Automation" -> select it

![image](https://github.com/user-attachments/assets/e3c207b7-8d81-4b29-bcb8-eac48e1b0357)

2. Click Add skill in [Your name]_Reorder_Automation

![image](https://github.com/user-attachments/assets/9d15eef2-297d-4057-b836-a8c1dfef30ab)

3. Map fields as image below

![image](https://github.com/user-attachments/assets/f33f18ca-3d8c-4fbf-8c83-97705099555e)

### Mapping guideline

```code
AccountId = [Get all accounts].[Id]
OrderDate = [2nd Input form].[Order Date]
UnitPrice = [Get all products].[Product_Amount]
Product2Id = [Get all products].[Id]
ReorderQty = [2nd Input form].[Reorder Quantity]
OrderStatus = [2nd Input form].[Order Status]
PriceBookId = [Get all price book].[Id]
```

## Publish skillflow

1. Click Action button -> Enhance

![image](https://github.com/user-attachments/assets/ae72c2e5-8a13-499d-aeee-24261adcccfa)

2. Set Description to ```Used when user wants to perform research on best supplier then automate order in Salesforce``` -> click Publish button

![image](https://github.com/user-attachments/assets/098abb74-7243-49e7-9291-f61305e7c986)

3. Go to Skill catalog page -> type "Skillflow" in search field -> click it once it is found -> type "[Your name]_Reorder_Skillflow" -> click Add skill in [Your name]_Reorder_Skillflow

![image](https://github.com/user-attachments/assets/8c5a00d3-93cc-4255-b371-424891afeba2)

4. Go to AI Agent Configurator page -> click Apps and skills on left pane -> search "skill flow" in search field -> click it once it is found -> type "[Your name]_Reorder_Skillflow" in search field -> once it is found, click Add to chat

![image](https://github.com/user-attachments/assets/b3b37d69-9f85-446c-bebe-6a71db3a63ce)

5. Modify description field -> click Add skill button

![image](https://github.com/user-attachments/assets/045b4134-f4ce-4aea-af73-84eceefaf0f4)


## Test skillflow

1. 
