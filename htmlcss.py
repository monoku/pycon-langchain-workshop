css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://cdn.discordapp.com/attachments/1070566005492940820/1117501439158263808/monoku_ai_Chatbot_icon_for_an_app_colorful_flat_illustration_b2678140-459d-4d86-9487-937ef0ee3e9c.png" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://cdn.discordapp.com/attachments/1070566005492940820/1117503426247524372/monoku_ai_Flat_design_app_icon_of_a_profile_picture_account_gen_11cef9ff-9c6e-4b93-84e5-906aced17586.png">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
