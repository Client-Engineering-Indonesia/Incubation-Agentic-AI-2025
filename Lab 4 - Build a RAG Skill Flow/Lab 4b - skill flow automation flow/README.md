# Objective

Now that we have all the skills and workflows in place, we can create a complete flow. You can create this flow within project or skill flow. Since Skill Flow is more readily available, we will build this final flow in the Skill Flows section.

## Create workflow to get supplier

1. Go to Skill studio -> open your workflow named [Your Name]_Reorder_Decision -> click Create skill button <img width="295" alt="image" src="https://github.com/user-attachments/assets/4edd2e53-29e8-4955-a8cd-7e9990d9fe59" /> in left-bottom side -> select Workflow -> set Name to [Your Name]_Get Supplier Flow

<img width="823" alt="image" src="https://github.com/user-attachments/assets/d3a4a237-2a25-4258-b9c5-7a7f3cfa03b6" />

2. Hover your mouse to line after Start Node -> click + button -> select Skill from catalog

<img width="252" alt="image" src="https://github.com/user-attachments/assets/a08f26b8-59c7-40f9-907b-8fbf263fc87c" />

3. Type "riset" in search field -> select "Riset Supplier"

<img width="1592" alt="image" src="https://github.com/user-attachments/assets/041ce149-5574-47f7-b250-e86ed105e28c" />

3. Select Supplier Research -> click Save button

<img width="1599" alt="image" src="https://github.com/user-attachments/assets/a66f2d8a-012b-4f7e-af33-8b3757c109ef" />

4. Go to Variables tab -> add variable named "query" and "response_message" with details as image below:

<img width="1405" alt="image" src="https://github.com/user-attachments/assets/967b9b0b-14b7-4e52-beb6-33dfa488cc43" />

5. Go back to Diagram tab -> click [Your Name]_Get Supplier Flow -> set Input mapping as image below:

<img width="1246" alt="image" src="https://github.com/user-attachments/assets/d81c2b69-4772-46a9-9557-e38b330d643d" />

6. Go to Output mapping tab -> set details as image below -> click OK button

<img width="1232" alt="image" src="https://github.com/user-attachments/assets/4f33211d-8911-4c5c-94aa-2240b47df771" />

7. Hover your mouse after Supplier Research node -> click + button -> select Generative AI

<img width="256" alt="image" src="https://github.com/user-attachments/assets/a5cca45d-6962-4ca6-907f-d2c709cdf9b0" />

8. Select Create Generative AI

<img width="254" alt="image" src="https://github.com/user-attachments/assets/047fa5dd-b239-4855-be4d-2e4b6e8f3c4b" />

9. Set Name to "Get Supplier Name Msg" -> click Crate button

<img width="829" alt="image" src="https://github.com/user-attachments/assets/4a3ba50a-ec22-4d3e-866a-e4748ee5cfa4" />

10. Set Prompt to ```Anda bertugas untuk melakukan identifikasi supplier yang dibutuhkan user berdasarkan rekomendasi yang diberikan``` -> add prompt variable named "recommendation" -> set Prompt input to ```rekomendasi: {{recommendation}} Hanya berikan supplier yang terbaik!``` -> set Model to "mistralai/mixtral-8x7b-instruct-v01" -> set Max generated token to 500 -> click Generate button to test -> ensure you have view as image below

<img width="1399" alt="image" src="https://github.com/user-attachments/assets/24aa5de7-83e8-48c9-a251-f9b34440447d" />

11. Click Get Supplier Name Msg node -> click Define data mapping button <img width="305" alt="image" src="https://github.com/user-attachments/assets/66e23316-692a-40fc-a319-3dcad41bdbfd" /> -> set Input mapping as image below

<img width="1240" alt="image" src="https://github.com/user-attachments/assets/a00881a4-fa8b-4e37-bfc0-19c6957369b6" />

12. Go to Output mapping -> map generated_text variable to suplier_name

<img width="1234" alt="image" src="https://github.com/user-attachments/assets/4d71bed8-d4e6-4cde-9873-e492cdf68c7d" />

13. Hover your mouse to Activity node -> click Delete icon

<img width="299" alt="image" src="https://github.com/user-attachments/assets/145c4b75-aaed-43db-a93d-3603d876c190" />
