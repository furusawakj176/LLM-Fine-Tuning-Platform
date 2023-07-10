import gradio as gr
import random
import time

with gr.Blocks() as demo:
    gr.Markdown("# LLM Fine-Tunning Platform")
    with gr.Tab("カスタムモデルの作成"):
        with gr.Row():      
            text_input = gr.Textbox(label="新規モデル名", info="新しく生成するカスタムモデルに名前をつけて下さい")
            gr.Dropdown(
                ["model1", "model2", "model3"], label="事前学習済みモデルの選択", info="使用する事前学習済みモデルを指定して下さい"
            )
        with gr.Row():
            text_output = gr.Textbox(label="データフォルダ", info="アップロード済み追加学習用データフォルダのパスを指定して下さい")
            generate_button = gr.Button("生成")

    with gr.Tab("モデルのテスト"):
        with gr.Row():
            chatbot = gr.Chatbot()
            with gr.Column():
                msg = gr.Textbox(label="入力")
                clear = gr.ClearButton([msg, chatbot])
            with gr.Column():            
                with gr.Row():
                    change_cb1 = gr.Checkbox(label="変更内容をモデルに反映させる")
                    send = gr.Button("デプロイ")
        
            def respond(message, chat_history):
                bot_message = random.choice(["よう！冒険者かい?", "オレも昔はあんたのような冒険者だったんだが", "膝に矢を受けてしまってな"])
                chat_history.append((message, bot_message))
                time.sleep(2)
                return "", chat_history

            msg.submit(respond, [msg, chatbot], [msg, chatbot])

    with gr.Tab("APIの公開と管理"):
            text_pjname = gr.Textbox(label="プロジェクト名")
            gr.Dropdown(
                ["my-model1", "my-model2", "my-model3"], label="モデルの選択", info="公開するカスタムモデルを指定して下さい"
            )
            deploy_button = gr.Button("デプロイ")

    with gr.Tab("設定・機能拡張"):
        with gr.Tab("インストール済み"):
          with gr.Row():
            text1 = gr.Markdown("https://hogehoge.hoge/test/test")
            btn1 = gr.Button("UnInstall")

        with gr.Tab("利用可能"):
          with gr.Row():
            text1 = gr.Markdown("https://hogehoge.hoge/test/test")
            btn1 = gr.Button("UpDate")

        with gr.Tab("URLからインストール"):
          with gr.Row():
            url1 = gr.Textbox("")
            btn1 = gr.Button("Install")

        with gr.Tab("設定"):
            select_cbgroup = gr.CheckboxGroup(["1st", "2nd", "3rd"])
            select_cb1 = gr.Checkbox(label="設定1")
            select_cb2 = gr.Checkbox(label="設定2")
            select_cb3 = gr.Checkbox(label="設定3")
            select_cb4 = gr.Checkbox(label="設定4")
            select_slider = gr.Slider(label="スライド式設定")

demo.launch()