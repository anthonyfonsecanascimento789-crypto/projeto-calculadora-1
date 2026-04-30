import streamlit as st
import calculadora as calc

numero1 = st.number_input("Digite o primeiro numero:", step=0.1, value=None)
numero2= st.number_input("Digite o segundo numero:", step=0.1, value=None)
operacao = st.selectbox("Selecione a operação:", ["+","-","/", "*"])


if st.button("Calcular"):
    resultado = calc.calcular(numero1, numero1, operacao)
    st.info(f"O resultado é:{resultado}")
