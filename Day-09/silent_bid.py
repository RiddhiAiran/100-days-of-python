import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Silent Auction",
    page_icon="🎯",
    layout="centered"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #1E88E5;
        font-size: 3rem !important;
        text-align: center;
        padding-bottom: 2rem;
    }
    .description {
        background-color: #E8F0FE;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 2rem;
        color: #1F1F1F;
        border: 1px solid #BFDBFE;
    }
    .description h2 {
        color: #1E40AF;
    }
    .description ul {
        color: #1F1F1F;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state variables
if "bids" not in st.session_state:
    st.session_state.bids = {}
if "current_page" not in st.session_state:
    st.session_state.current_page = "bid_form"
if "show_winner" not in st.session_state:
    st.session_state.show_winner = False
if "bidder_count" not in st.session_state:
    st.session_state.bidder_count = 0

# Callback functions
def submit_bid():
    if st.session_state.name_input and st.session_state.bid_input > 0:
        st.session_state.bids[st.session_state.name_input] = st.session_state.bid_input
        st.session_state.bidder_count += 1
        st.session_state.current_page = "confirmation"

def next_bidder():
    st.session_state.current_page = "bid_form"

def finish_auction():
    st.session_state.show_winner = True
    st.session_state.current_page = "results"

def find_winner():
    if st.session_state.bids:
        highest_bid = max(st.session_state.bids.values())
        winner = [name for name, bid in st.session_state.bids.items() if bid == highest_bid][0]
        return winner, highest_bid
    return None, None

# Main UI with dark blue title for visibility
st.markdown("<h1 style='text-align: center; color: #1E40AF;'>🎯 Silent Auction Bid</h1>", unsafe_allow_html=True)

# Introduction and Rules Section with improved contrast
st.markdown("""
    <div class="description">
        <h2 style='text-align: center; color: #1E40AF;'>Welcome to the Silent Auction! 🎉</h2>
        <p style='text-align: justify; color: #1F1F1F;'>
            A silent auction is an exciting way to bid on items where all bids remain secret until the end. 
            Here's how it works:
        </p>
        <ul style='color: #1F1F1F;'>
            <li><strong>Step 1:</strong> Enter your name and your bid amount</li>
            <li><strong>Step 2:</strong> Your bid will be kept completely confidential</li>
            <li><strong>Step 3:</strong> Each bidder will place their bid</li>
            <li><strong>Step 4:</strong> The highest bidder wins!</li>
            <li><strong>Final Step:</strong> Only the winner's name will be revealed at the end</li>
        </ul>
        <p style='text-align: center; font-weight: bold; color: #1E40AF;'>
            May the best bid win! 🏆
        </p>
    </div>
""", unsafe_allow_html=True)

# Bid Form Page
if st.session_state.current_page == "bid_form":
    st.markdown("### 📝 Place Your Bid")
    with st.form(key="bid_form"):
        st.text_input("Enter your name:", key="name_input", 
                     placeholder="Your name here...")
        st.number_input("Enter your bid:", min_value=0, step=1, key="bid_input",
                       help="Enter your best bid amount in dollars")
        submit_button = st.form_submit_button("Submit Bid 🎯", on_click=submit_bid)

# Confirmation Page
elif st.session_state.current_page == "confirmation":
    st.success("🎉 Bid submitted successfully!")
    col1, col2 = st.columns(2)
    with col1:
        st.button("Next Bidder 👤", on_click=next_bidder)
    with col2:
        st.button("Finish Auction 🏁", on_click=finish_auction)

# Results Page with improved contrast
elif st.session_state.current_page == "results":
    winner, highest_bid = find_winner()
    if winner:
        st.balloons()
        st.markdown(f"""
            <div style='background-color: #E8F0FE; padding: 20px; border-radius: 10px; text-align: center; border: 1px solid #BFDBFE;'>
                <h2 style='color: #1E40AF;'>🎉 Auction Results 🎉</h2>
                <p style='font-size: 1.5rem; color: #1F1F1F;'>
                    Congratulations! The winner is <strong>{winner}</strong>
                </p>
                <p style='font-size: 1.2rem; color: #1F1F1F;'>
                    Winning Bid: <strong>${highest_bid}</strong>
                </p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("No bids have been placed yet.")
    
    # Option to start new auction
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Start New Auction 🔄"):
        st.session_state.bids = {}
        st.session_state.current_page = "bid_form"
        st.session_state.show_winner = False
        st.session_state.bidder_count = 0
        st.rerun()

# Sidebar with auction status - improved contrast
if st.session_state.bids:
    st.sidebar.markdown("""
        <div style='background-color: #E8F0FE; padding: 10px; border-radius: 5px; border: 1px solid #BFDBFE;'>
            <h3 style='color: #1E40AF; text-align: center;'>Auction Status</h3>
            <p style='text-align: center; font-size: 1.2rem; color: #1F1F1F;'>
                Total Bids: {}</p>
        </div>
    """.format(len(st.session_state.bids)), unsafe_allow_html=True)