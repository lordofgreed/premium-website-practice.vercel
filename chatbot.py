import sys
import json
import random

# List of engaging, friendly conversational prefixes to make the bot feel alive and warm
INTRO_PHRASES = [
    "Hello! I'd be absolutely delighted to help you with that. ✨",
    "Great question! Here's the scoop: 🚀",
    "I've got the perfect answer for you! 🌟",
    "No problem at all, let me clear that up for you! 🛡️",
    "Aha! Let me look into that for you. 🔍"
]

OUTRO_PHRASES = [
    "\n\nHope this helps! Let me know if you need anything else. 🤝",
    "\n\nDoes that make sense? Let me know if I can assist with anything else! 🌸",
    "\n\nI'm always here if you have more questions. Stay legendary! 👑",
    "\n\nLet me know if you'd like me to guide you through anything else. ⚡"
]

def get_bot_reply(message):
    lower_msg = message.lower().strip()
    
    # Help/Menu Trigger
    if lower_msg in ["help", "menu", "options", "what can you do", "?", "commands"]:
        return (
            "👋 Welcome to **OGhaitong Premium Support**!\n\n"
            "I'm your intelligent virtual gaming-concierge assistant. Here is what you can ask me about:\n"
            "• 📦 **Shipping & Delivery** — *rates, processing, and speed*\n"
            "• 📍 **Track Order** — *find out where your gear is*\n"
            "• 🛑 **Cancel Order** — *cancellation policy & steps*\n"
            "• 💸 **Discounts & Promos** — *active coupons and offers*\n"
            "• 🔄 **Returns & Refunds** — *our hassle-free 30-day policy*\n"
            "• 🛡️ **Warranty Support** — *device hardware protection details*\n"
            "• 🎮 **Esports & Gaming** — *Mobile Legends triggers, FAI8 Pro League gear*\n"
            "• 🎧 **Audio Gear** — *Aura Unleashed Pro specs & ANC features*\n"
            "• 💳 **Payment Methods** — *Razorpay checkout support*\n"
            "• 👤 **Human Support** — *how to talk directly to our team*\n\n"
            "Just type any keyword or ask me a question naturally!"
        )

    # --- NEW ADDITIONS: Specific E-commerce Workflows ---
    
    # Order Tracking
    if "where is my order" in lower_msg or "status" in lower_msg or ("track" in lower_msg and "order" in lower_msg):
        main_reply = (
            "I can certainly help you track your gear! 📦📍\n\n"
            "To give you the most accurate update, could you please reply with your **Order ID**? "
            "(It usually starts with 'OG' and can be found in your confirmation email).\n\n"
            "Once you provide that, I'll fetch the exact location of your package!"
        )
    
    # Order Cancellation
    elif "cancel" in lower_msg:
        main_reply = (
            "I understand you'd like to cancel your order. Let's see what we can do. 🛑\n\n"
            "• **Timeframe:** Orders can be easily cancelled for a full refund within **2 hours** of placement, before they hit our dispatch queue.\n"
            "• **Next Step:** Please reply with your **Order ID** and your reason for cancelling. I will process this immediately (or route it to a human agent if your order is already packed!)."
        )
        
    # Promo Codes & Discounts
    elif "discount" in lower_msg or "promo" in lower_msg or "coupon" in lower_msg or "offer" in lower_msg:
        main_reply = (
            "Who doesn't love a good deal? 💸\n\n"
            "• **Current Offer:** Use code **OGGAMER10** at checkout for 10% off your entire order!\n"
            "• **Newsletter:** Subscribe to our email newsletter at the bottom of our website to get an exclusive 15% off coupon for your first purchase.\n"
            "• **How to Apply:** Just paste your code into the 'Promo Code' box during the Razorpay checkout process."
        )

    # Restock / Out of Stock
    elif "restock" in lower_msg or "out of stock" in lower_msg or "available" in lower_msg:
        main_reply = (
            "Eyeing some gear that's currently sold out? Don't worry! 🛒\n\n"
            "• **Restock Alerts:** The best way to know when an item is back is to visit the product page and click the **'Notify Me'** button.\n"
            "• **Timeline:** Our premium esports gear usually restocks within **10-14 business days** depending on manufacturing cycles."
        )

    # Wrong or Missing Items
    elif "wrong item" in lower_msg or "missing" in lower_msg:
        main_reply = (
            "Oh no! I am so sorry to hear there's an issue with your delivery. Let's fix this immediately. 🛠️\n\n"
            "• **What to do:** Please email **support@oghaitong.com** with your **Order ID** and a **clear photo** of what you received (and the packaging).\n"
            "• **Resolution:** Our human priority team will review it right away and dispatch the correct/missing items via express shipping, on the house!"
        )

    # --- CORE MODULES (Original logic retained and slightly optimized) ---
    
    elif "shipping" in lower_msg or "delivery" in lower_msg:
        main_reply = (
            "We offer **Free Standard Global Shipping** on all premium vault items! 📦\n\n"
            "• **Delivery Timeline:** Usually takes **3 to 5 business days** depending on your region.\n"
            "• **Tracking:** As soon as your package is dispatched, we send a unique tracking ID to your registered email.\n"
            "• **Packaging:** Every premium order is shipped in secure, anti-static custom vault packaging to keep your gear safe."
        )
    elif "return" in lower_msg or "refund" in lower_msg or "exchange" in lower_msg:
        main_reply = (
            "We want you to be 100% thrilled with your purchase! 🔄\n\n"
            "• **30-Day Policy:** Our policy allows returns/exchanges within 30 days of delivery.\n"
            "• **Condition:** Items must be in pristine, unused condition with original custom packaging.\n"
            "• **How to start:** Simply drop a message to support@oghaitong.com with your Order ID, and we will send you a pre-paid return label immediately."
        )
    elif "warranty" in lower_msg or "repair" in lower_msg or "broken" in lower_msg:
        main_reply = (
            "We back our products to the absolute limit! 🛡️\n\n"
            "• **1-Year Warranty:** All official OGhaitong gear comes with a **1-Year Limited Hardware Warranty**.\n"
            "• **What is covered:** Any manufacturing defects, firmware bugs, or hardware malfunction under normal usage conditions.\n"
            "• **Rapid Swap:** If we confirm a defect, we'll ship you a brand-new replacement unit with express shipping, free of charge."
        )
    elif "contact" in lower_msg or "human" in lower_msg or "support" in lower_msg or "email" in lower_msg:
        main_reply = (
            "Need to talk to a real human? We've got your back! 🤝\n\n"
            "• **Email Support:** You can write to our human squad at **support@oghaitong.com** anytime.\n"
            "• **Response Time:** We pride ourselves on resolving priority emails within **2 to 4 hours**.\n"
            "• **Account Console:** You can also open a priority support ticket directly inside your user dashboard for real-time tracking."
        )
    elif "esports" in lower_msg or "gaming" in lower_msg or "mobile legends" in lower_msg or "trigger" in lower_msg or "pubg" in lower_msg:
        main_reply = (
            "Gear up for tournament-level domination! 🎮🔥\n\n"
            "• **FAI8 & AuraHILLS Scrims:** Our gaming hardware is fully optimized for Mobile Legends: Bang Bang and PUBG Mobile esports standard.\n"
            "• **Tactical Triggers:** We design zero-latency conductive mobile triggers with mechanical micro-switches for tactile feedback.\n"
            "• **Cryo-Cooling:** Check out our active cryo-cooling fans to keep your device ice-cold during prolonged tournament matches!"
        )
    elif "audio" in lower_msg or "headphone" in lower_msg or "latency" in lower_msg or "bluetooth" in lower_msg or "anc" in lower_msg:
        main_reply = (
            "Immerse yourself in ultra-low latency acoustic perfection! 🎧⚡\n\n"
            "• **Aura Unleashed Pro:** Our signature headset features custom-tuned 40mm beryllium drivers.\n"
            "• **Active Noise Cancelling:** Advanced hybrid ANC blocks up to **42dB** of ambient noise.\n"
            "• **Zero-Latency Connection:** Powered by **Bluetooth 5.4** and low-latency gaming mode (under 40ms) so you never miss a sound cue."
        )
    elif "payment" in lower_msg or "razorpay" in lower_msg or "card" in lower_msg or "upi" in lower_msg:
        main_reply = (
            "We accept a wide variety of safe and secure payment options! 💳🔒\n\n"
            "• **Razorpay Gateway:** All transactions are secured with military-grade 256-bit encryption.\n"
            "• **Supported Methods:** Major Credit/Debit cards (Visa, MasterCard, RuPay), UPI, Net Banking, and popular wallets.\n"
            "• **Troubleshooting:** If your transaction fails but money gets deducted, do not worry! Razorpay auto-refunds failed checks in 2-3 business days."
        )
    elif any(greeting in lower_msg for greeting in ["hello", "hi", "hey", "greetings", "yo"]):
        return (
            "👋 **Hello there, champion!**\n\n"
            "I'm your official **OGhaitong Support AI**. I'm here to help you configure, troubleshoot, or buy your next-gen gear!\n\n"
            "Feel free to ask me questions like:\n"
            "• *\"Where is my order?\"*\n"
            "• *\"Tell me about the 30-day return policy.\"*\n"
            "• *\"What gaming accessories do you have?\"*\n\n"
            "How can I level up your shopping experience today? ⚡"
        )
    else:
        # Default fallback response
        return (
            "Thanks for reaching out! 💬\n\n"
            "I couldn't find direct matches in my core modules for that specific question, but I'm learning more every day!\n\n"
            "For active orders, custom delivery tracking, or specific technical troubleshooting, please contact our expert human team directly at **support@oghaitong.com** or open a priority ticket in your account dashboard. 🤝"
        )

    # Wrap matching responses with dynamic intro and outro phrases to feel alive
    intro = random.choice(INTRO_PHRASES)
    outro = random.choice(OUTRO_PHRASES)
    return f"{intro}\n\n{main_reply}{outro}"

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            user_msg = sys.argv[1]
        else:
            # Read from stdin
            input_data = sys.stdin.read()
            try:
                js = json.loads(input_data)
                user_msg = js.get("message", "")
            except:
                user_msg = input_data.strip()
        
        reply = get_bot_reply(user_msg)
        print(json.dumps({"reply": reply}))
    except Exception as e:
        print(json.dumps({"reply": f"Error running chatbot script: {str(e)}", "error": True}))
