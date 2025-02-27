import streamlit as st
from services.blob_service import upload_blob

def configure_interface():
    st.title("Upload de arquivos DIO - Desafio 1 - Azure - FakeDocs")
    uploaded_file = st.file_uploader('Escolha um arquivo:', type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        fileName = uploaded.file.name
        # Enviar para o blob storage
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
          st.write(f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storage")
          credit_card_info = ""
          show_image_and_validation(blob_url, credit_card_info)
        else:
          st.write(credit_card_info)


def show_image_and_validation(blob_url, credit_card_info):
  st.image(blob_url, caption="imagem enviada", use_column_width=True)
  st.write("Resultado da validação")
  if credit_card_info and credit_card_info["card_name"]:
    st.markdown(f"<h1 style='color: green;' >Cartão Válido </h1>", unsafe_allow_html=True)
    st.write(f"Nome do Titular {credit_card_info['card_name']}")
    st.write(f"Banco Emissor {credit_card_info['bank_name']}")
    st.write(f"Data da validade {credit_card_info['expiry_date']}")
  else:
    st.markdown(f"<h1 style='color: red;' >Cartão Inválido </h1>", unsafe_allow_html=True)
    st.write("Este não é um cartão válido")




if __name__ == "__main__":
    configure_interface()


