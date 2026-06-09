def calculate_ast(postcode):
    now = time.gmtime(time.time())
    lth = now.tm_hour + now.tm_min / 60 + now.tm_sec / 3600    
    n = now.tm_yday
    
    nomi = pg.Nominatim('gb')
    result = nomi.query_postal_code(postcode)
    long = result.longitude
    
    B = np.radians((360 / 364) * (n - 81))
    eot = 9.87 * np.sin(2 * B) - 7.53 * np.cos(B) - 1.5 * np.sin(B)
    
    long_cor = 4 * long
    ast = (lth + eot/60 + long_cor/60) % 24

    hours = int(ast)
    minutes = int((ast - hours) * 60)
    seconds = int((((ast - hours) * 60) - minutes) * 60)
    return(f"{hours:02d}:{minutes:02d}:{seconds:02d}")

st.title("Apparent Solar Time Calculator")
postcode = st.text_input("Please enter a UK postcode")
if st.button ("Calculate"):
    result = calculate_ast(postcode)
    st.success(f"The Apparent Solar Time is {result}")
