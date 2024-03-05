from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     title = page.locator("Title")

#    # We assert that it has the text "This is the homepage."
#     expect(title).to_have_text("MakersBnB")

# check /spaces route works

def test_get_all_spaces(page, test_web_address, db_connection, web_client):
    db_connection.seed('seeds/spaces_table.sql')
    page.goto(f'http://{test_web_address}/spaces')
    response = web_client.get('/spaces')
    assert response.status_code == 200
    div_tags = page.locator('div')
    expect(div_tags).to_have_text([
        'Name: Wizarding Cupboard\nLocation: London',
        'Name: Amore Penthouse\nLocation: Paris',
        'Name: Paella Place\nLocation: Madrid',
        'Name: Mi Casa\nLocation: Madrid'
    ])

# check each individual space on /spaces/<space_id>

def test_get_individual_space(page, test_web_address, db_connection, space_id=1):
    db_connection.seed('seeds/spaces_table.sql')
    page.goto(f'http://{test_web_address}/spaces/{space_id}')
    header = page.locator('h1')
    expect(header).to_have_text('Wizarding Cupboard')


# def test_get_album_1(page, test_web_address, db_connection, album_id=1):
#     db_connection.seed('seeds/music_library.sql')
#     page.goto(f'http://{test_web_address}/albums/{album_id}')
#     header = page.locator('h1')
#     album_info = page.locator('p')
#     expect(header).to_have_text('Doolittle')
#     expect(album_info).to_have_text('Release year: 1989\nArtist: Pixies')