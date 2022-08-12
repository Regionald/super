# Set your secret key. Remember to switch to your live secret key in production.
# See your keys here: https://dashboard.stripe.com/apikeys
import stripe
stripe.api_key = "sk_test_51KsjcJC0Dcb2F5YQXaeiCbF6GhqivBzXdlWVtOSOKaa9r3ZALnmwVFj2ueD31BjzSsfaKUDX1Qc4Jr0IJhUCNNGl00wiPtvViJ"

stripe.Account.create(type="standard")