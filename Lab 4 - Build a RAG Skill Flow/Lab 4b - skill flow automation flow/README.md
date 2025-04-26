![image](https://github.com/user-attachments/assets/b06eee3f-2a75-4849-93d8-4d3c9576fe31)# Objective

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

![image](https://github.com/user-attachments/assets/a8a01b47-6860-4e69-b3ec-f647c2f64647)

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

13. Set Context to ```Anda adalah asisten untuk tim pengadaan yang memberikan jawaban sesuai dengan prompt user``` -> add prompt variabled named "research" -> set Max generated token to 500 -> change model to mistralai/mixtrail-8x7b-instruct-v01 -> set Prompt input to ```Berikan satu nama supplier terbaik berdasarkan hasil riset di bawah ini. Hanya berikan nama supplier saja tidak perlu diberikan penjelasan. Hasil Riset: {{research}}```

![image](https://github.com/user-attachments/assets/48274b64-ebdb-4965-ac54-83290a6ab482)

14. Go to your previous workflow -> click Define data mapping button ![image](https://github.com/user-attachments/assets/aa31174d-7ec2-4f02-8ce7-0fef44dbd79c) -> map variables under Input mapping tab as image below

![image](https://github.com/user-attachments/assets/30c404a6-9916-494d-9c1b-d3795e202341)

15. Go to Output mapping tab -> set variable as image below -> click OK button

![image](https://github.com/user-attachments/assets/6bbfb4c6-199c-4352-9cf9-941cde7c4d71)

16. Ensure you have set visibility of your workflow to Public

![image](https://github.com/user-attachments/assets/91ddfa4c-7599-4b29-b14d-ab3f3a4a67d7)

17. Click Publish button ![image](https://github.com/user-attachments/assets/e4354400-5652-496b-9fab-5a317164e40a) -> set Name to "test-version-01" -> click Create version and publish button

![image](https://github.com/user-attachments/assets/ca06cd6b-4d42-4e93-a085-0a90d8ef8c5e)

##
