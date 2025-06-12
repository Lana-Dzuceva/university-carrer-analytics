css = """
<style>
    .header {
        background-color: #E57373;
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 2rem;
    }
    .footer {
        background-color: rgba(0, 0, 0, 0.1);
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        font-size: 0.9rem;
        color: #4A4A4A;
        bottom: 0;
        width: 100%;
        left: 0;
    }
    .footer a {
        color: #E57373;
        text-decoration: none;
        margin: 0 0.5rem;
    }
    .footer a:hover {
        text-decoration: underline;
    }
    .stTextInput> div> div> input {
        border: 1px solid ;
        border-radius: 5px;
        padding: 0.5rem;
        color: #4A4A4A;
    }
    .stTextInput> div> div> input:disabled {
        background-color: #F5F5DC;
        color: #4A4A4A;
    }
    .vacancy-box {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
        color: #4A4A4A;
    }
    .stApp {
        background-color: rgba(0, 0, 0, 0.02);
        min-height: 90vh;
        display: flex;
        flex-direction: column;
    }
    .main-content {
        flex: 1;
        padding-bottom: 1rem; /* Отступ для футера */
    
        width: 100%; /* Контент занимает всю доступную ширину контейнера */
        max-width: none; /* Убираем ограничения по максимальной ширине */
    }

    .appview-container .main .block-container{
       width: 100%;
         }
</style>
"""
#     .main > div {
#         padding-left: 130px;
#         padding-right: 130px;
#     }