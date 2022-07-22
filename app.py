from conf import page_set
#conf.page_set()
page_set()

import streamlit as st
from multiapp import MultiApp
from apps import TEST

app = MultiApp()


app.add_app("TEST", TEST.app)

# The main app
app.run()


