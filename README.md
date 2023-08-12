# Cal Poly Cat Program

### A cat directory made for the [Cal Poly Cat Program (CPCP)](https://catprogram.calpoly.edu/)

<span>
  <img src="https://user-images.githubusercontent.com/18134219/87235554-b068d500-c3a2-11ea-97f4-bd4939c150d6.png" width="48%" />
  <img src="https://user-images.githubusercontent.com/18134219/87235553-ae9f1180-c3a2-11ea-87d1-f74858867a39.png" width="48%" />
</span>

The [Cal Poly Cat Program (CPCP)](https://catprogram.calpoly.edu/) is a non-profit organization of students, faculty, staff and community members who care about the health and happiness of both feral and domesticated cats. This software was made to decrease logistical friction (they were using paper filing and a large excel sheet) so they could focus on helping the cats. This site is currently live [here](https://cpcp-cats.herokuapp.com/).

There is also an accompanying mobile app for this site! The repository can be [found here](https://github.com/finlaylp/SLO_cat_shelter_mobile).

## The Team
- Sydney Nguyen [@syddaddie](https://www.instagram.com/syddaddie/) - Designer
- Finlay Piroth [@finlaylp](https://github.com/finlaylp) - Mobile Developer
- Jillian Quinn [@JillianQuinn](https://github.com/JillianQuinn) - Mobile Developer
- Jay Sung [@jaysungl42](https://github.com/jaysungl42) - Frontend Developer
- Evan Witulski [@ewitulsk](https://github.com/ewitulsk) - Backend Developer
- Ethan Zimbelman [@Zimboboys](https://github.com/Zimboboys) - Team Lead / Full Stack Developer

## Getting Started
The web portion of this application was made in Django. The following will assume you have Python, Django, and pip installed.

1. Clone the repo `git clone https://github.com/hack4impact-calpoly/calpoly-cat-program`
2. Install postgresql &nbsp;&nbsp; [ [Mac OS](https://www.postgresql.org/download/macosx/) | [Windows](https://www.postgresql.org/download/windows/) |  [Linux](https://www.postgresql.org/download/linux/) ]
3. Move into the directory by using `cd calpoly-cat-program` and install the dependancies `pip install -r requirements.txt`
4. Configure the environment variables in `.defaultenv` and rename it to `.env`
5. From the command line, run `python manage.py migrate`, then `python manage.py runserver`
6. Hopefully the site is up and you can visit it at [localhost:8000](http://localhost:8000)

### Deployment
This site is deployed on Heroku, which is nice because it is free, but not nice because it [won't store files long term](https://help.heroku.com/K1PPS2WM/why-are-my-file-uploads-missing-deleted). To get around this, we use s3 for file storage. This should be fine because s3 is cheap.

Note: Deploying with static files on Heroku is difficult. Keep the server in DEBUG=True mode to counter this

To setup s3 file storage, do the following. This assumes you have an AWS account.

1. Create an IAM user with the AmazonS3FullAccess policy attached
2. Copy these credentials into your `.env`
3. Create an S3 bucket and [enable CORS](https://docs.aws.amazon.com/AmazonS3/latest/dev/cors.html#how-do-i-enable-cors)
4. Copy the bucket name to your `.env` file and change ISPROD to True
5. Start the web server
