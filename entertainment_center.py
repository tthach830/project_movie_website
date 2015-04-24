import media
import webbrowser
import fresh_tomatoes

#creates 6 movie objects with 7 parameters: Title,Director,Writers,Starring,storylinfo, image url,trailer youtube url
interstellar = media.Movie("Interstellar",
                     "Director: Christopher Nolan",
                     "Writers: Christopher Nolan, Jonathan Nolan",
                    "Starring: Matthew McConaughey, Anne Hathaway, Jessica Chastain",
                    "In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable. Professor Brand (Michael Caine), a brilliant NASA physicist, is working on plans to save mankind by transporting Earth's population to a new home via a wormhole.",
                     "http://blog.buecher.de/wp-content/uploads/2014/11/Interstellar.jpg",
                     "https://www.youtube.com/watch?v=0vxOhd4qlnA")

Jupiter_Ascending = media.Movie("Jupiter Ascending",
                     "Directors: Lana Wachowski, Andy Wachowski Writers: Andy Wachowski, Lana Wachowski",
                    "Writers: Andy Wachowski, Lana Wachowski",
                                "Starring: Mila Kunis, Channing Tatum, Sean Bean",
                                "Jupiter Jones (Mila Kunis) was born under signs that predicted future greatness, but her reality as a woman consists of cleaning other people's houses and endless bad breaks. Caine (Channing Tatum), a genetically engineered hunter, arrives on Earth to locate her, making Jupiter finally aware of the great destiny that awaits her: Jupiter's genetic signature marks her as the next in line for an extraordinary inheritance that could alter the balance of the cosmos.",
                     "http://ia.media-imdb.com/images/M/MV5BMTQyNzk2MjA2NF5BMl5BanBnXkFtZTgwMjEwNzk3MjE@._V1_SX214_AL_.jpg",
                     "www.youtube.com/watch?v=EVZELMRXeYM")

Edge_Of_Tomorrow = media.Movie("Edge of Tomorrow",
                            "Director: Doug Liman",
                              "Writers: Jez Butterworth, Chris. McQuarrie, John Butterworth",
                               "Starring: Tom Cruise, Emily Blunt, Brendan Gleeson",
                     "Major Cage is demoted and dropped into combat. He is killed, managing to killed an alpha alien. He awakens back at the beginning of the same day and is forced to fight and die again..",
                    "https://image.tmdb.org/t/p/w300/jseO7IBq4g0IZu0cCpJiOffjx42.jpg",
                     "https://www.youtube.com/watch?v=vw61gCe2oqI")

iRobot = media.Movie("I, Robot",
                     "Director: Alex Proyas",
                     "Writers: Jeff Vintar, Akiva Goldsman, Isaac Asimov",
                     "Starring: Will Smith, Bridget Moynahan, Alan Tudyk",
                     "In 2035, highly intelligent robots fill public service positions throughout the world, operating under three rules to keep humans safe. Despite his dark history with robotics,",
                    "http://upload.wikimedia.org/wikipedia/en/3/3b/Movie_poster_i_robot.jpg",
                    "https://youtu.be/XtG-vK88K0Q")
Species3 = media.Movie("Species 3",
                       "Director: Brad Turner",
                       "Writer: Ben Ripley",
                       "Starring: Natasha Henstridge, Sunny Mabrey, Robert Knepper",
                       "After she delivers her child in an ambulance, alien Eve (Natasha Henstridge) is killed by a half-breed. Fortunately, Dr. Abbot (Robert Knepper) scoops up the baby alien and escapes",
                       "http://www.gstatic.com/tv/thumb/dvdboxart/35126/p35126_d_v7_aa.jpg",
                       "https://youtu.be/ia_Ev8I_5II")
Big_Hero_6 = media.Movie("Big Hero 6",
                         "Directors: Don Hall, Chris Williams",
                         "Writers: Dan Gerson, Jordan Roberts, Robert L. Baird",
                         "Starring: Scott Adsit, Ryan Potter, Daniel Henney",
                        "The special bond that develops between plus-sized inflatable robot Baymax, and prodigy Hiro Hamada, who team up with a group of friends to form a band of high-tech heroes.",
                         "http://static.rogerebert.com/uploads/movie/movie_poster/big-hero-6-2014/large_big_hero_six_ver2.jpg",
                         "www.youtube.com/watch?v=z3biFxZIJOQ")

#create/store an array/list  of the movies above
movies=[Edge_Of_Tomorrow,Species3,iRobot,Big_Hero_6,Jupiter_Ascending,interstellar]
#generate fresh_tomatoes.html from the list: moviess
fresh_tomatoes.open_movies_page(movies)
