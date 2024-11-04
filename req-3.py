import os
from openai import OpenAI
import tiktoken
import pickle
client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
)

# Choose a model or encoding. Common models include 'gpt-3.5-turbo', 'gpt-4', etc.
model_name = 'gpt-4o-mini'

# Load the encoding for the model
encoding = tiktoken.encoding_for_model(model_name)

text = \
"""```
<!-- Source: index_split_002.html -->
<p class=\"block_2\">???: \u201cTake <i class=\"calibre4\">aim</i>!\u201d</p>
<p class=\"block_2\">Next, the eyes of one of the remaining heads of the Blight Dragon were pierced by an arrow of divine speed.</p>
<p class=\"block_2\">It was a small target when compared to the large build of the Blight Dragon, but the Chieftain of the People of Shudraq had magnificently shot through it, then sharply calling out to the two by her side.</p>
<p class=\"block_2\">Among the two who were called upon, one aligned the aim by eye measurement, and the other used her entire body to draw a huge bow that would have taken ten regular people to pull.</p>
<p class=\"block_2\">???: \u201cLet\u2026 it have <i class=\"calibre4\">it</i>!!\u201d</p>
<p class=\"block_2\">???: \u201cTake it <i class=\"calibre4\">down</i>~!!\u201d</p>
<p class=\"block_2\">The two of them combined their efforts to wield the powerful bow, and with a loud sound akin to a star being pierced, they landed a direct hit on the blinded head of the Blight Dragon, blasting everything above the jaw completely away, and reducing the Three-Headed-turned-Two-Headed even further into the One-Headed.</p>
<p class=\"block_2\">Valgren: \u201c\u2015\u2015\u2015\u2015KRUUUUUUUAGH!!\u201d</p>
<p class=\"block_2\">On top of that, having lost both its left and right heads, Valgren looked up to the sky as it generated tremendous heat within its large black body.</p>
<p class=\"block_2\">A breath of destruction, so synonymous with Dragons themselves, was turned towards the Fortified City below\u2015\u2015 At that moment, the eyes of the crazed Blight Dragon were met by the eyes of someone watching it from inside the great fortress that it was supposed to capture.</p>
<p class=\"block_2\">As that someone stood by that window, they directed their hand towards the Blight Dragon as it tore off the thorns within the skies\u2015\u2015</p>
<p class=\"block_2\">???: \u201c\u2015\u2015El Fula.\u201d</p>
<p class=\"block_2\">If an objective could be accomplished with minimal toil, neither flashy magic nor outlandish monstrous strength were necessary.</p>
<p class=\"block_2\">With precision that could serve as an example for all such things, the Blight Dragon\u2019s final remaining head was severed by a blade of wind possessing unrelenting sharpness.</p>
<p class=\"block_2\">Valgren: \u201c\u2015\u2015\u2015\u2015\u201d</p>
<p class=\"block_2\">Each of its three heads lopped off, the Blight Dragon falleth.</p>
<p class=\"block_2\">Such was the pathetic defeat of the Three-Headed Valgren, intended to be the trump card played by the undead forces.</p>
<p class=\"block_12\">\u25b3\u25bc\u25b3\u25bc\u25b3\u25bc\u25b3</p>
<p class=\"block_2\">???: \u201cImpossible, impossibleimpossibleimpossibleimpossibleimpossibleimpossibleimpossibleimpossible\u2026!\u201d</p>
<p class=\"block_2\">His body trembling all over, while scratching at his hair, Palladio could not accept the defeat of Valgren which he had just witnessed occur through his Evil Eye.</p>
<p class=\"block_2\">Things that ought to have been impossible, continued to occur one after another.</p>
<p class=\"block_2\">Because of that, Palladio fell from what had been an overwhelmingly advantageous position; his pride wounded as one who ought to have been leisurely waging the warfare of a true Emperor, he tasted humiliation.</p>
<p class=\"block_2\">Palladio: \u201cHow!? How have they seen through all of mine plans!\u201d</p>
<p class=\"block_2\">The surprise tactic of having the undead flying dragon riders carry a dragonship and cross over the mountain, was perfect.</p>
<p class=\"block_2\">He was not certain if that had been anticipated, or if it had been preserved fighting assets that immediately reacted to it, but the surprise tactic had been thwarted. Only, that was something neither unpleasant nor fatal\u2015\u2015 Rather, it ought not have been.</p>
<p class=\"block_2\">Palladio: \u201cWhat even is the Blight Dragon, THE THREE-HEADED\u2026!\u201d</p>
<p class=\"block_2\">The Three-Headed Valgren had immediately been sent out as a harbinger of despair\u2015\u2015 in the past, it had exerted tyranny in the accursed neighboring nation, the Kingdom of Lugunica, the resurrected fearsome Blight Dragon.</p>
<p class=\"block_2\">If that Dragon of forgone mind were to display its true worth, dominance through means of might and fear would have been accomplished.</p>
<p class=\"block_2\">To think that the mighty Valgren would be subjugated in such a manner, its three heads lopped off.</p>
<p class=\"block_2\">Palladio: \u201cWhy are the lot of you all so asinine!? Why be you unable to fulfill the duties expected of mine limbs!?\u201d</p>
<p class=\"block_2\">The fallen Blight Dragon, the failed ambush corps, the swarms of undead still having trouble conquering the first wall, each of them had failed to provide utility to Palladio, a cluster of fools who only continued to drag down on his legs.</p>
<p class=\"block_2\">When he took a moment to think about it, Vincent, Prisca, and Lamia all had possessed competent servants in their service.</p>
<p class=\"block_2\">In other words, the difference between Palladio, Vincent, and the rest, came down to whether they were blessed with servants or not. They had nothing to do with the strength of the person in question, and were naught more than external decorations.</p>
<p class=\"block_2\">Flaunting that, they were a shameless bunch unworthy of being a part of the Imperial Family attempting to outrival Palladio.</p>
<p class=\"block_2\">Palladio: \u201cThe Emperor of the Briar\u2019s solitary nature is the unmistakable true desire of Vollachian Emperor. I shall never stoop to the methods of you cowardly lot\u2026!\u201d</p>
<p class=\"block_2\">Even in the past Imperial Selection Ceremony, Vincent had avoided the stratagem that Palladio had formulated, and outsmarted him, snatching victory through such means.</p>
<p class=\"block_2\">The same thing was happening again\u2015\u2015 Palladio could not overlook such an outrageous act.</p>
<p class=\"block_2\">Palladio: \u201cAnybody, offer up a suggestion! As of now, I shall enact anything!\u201d</p>
<p class=\"block_2\">While burning with humiliation, Palladio loudly called out to the undead encampment.</p>
<p class=\"block_2\">In truth, Palladio had wished to persist as a solitary Emperor who asked not for the likes of others\u2019 opinions. But, the opponent had taken advantage of Palladio\u2019s haughtiness, wielding a spear of malice.</p>
<p class=\"block_2\">In that case, Palladio had no choice but to display the might of the Emperor through severity.</p>
<p class=\"block_2\">Palladio: \u201cIs there anyone!? Raise your voice! Or else\u2026\u201d</p>
<p class=\"block_2\">???: \u201c\u2015\u2015Well then, with your permission.\u201d</p>
<p class=\"block_2\">Turning his head, Palladio looked over the personnel of poor complexion, and a single person raised their voice.</p>
<p class=\"block_2\">At a glance, it was a slender figure, slowly walking through the crowd of undead\u2015\u2015 witnessing an aura peculiarly different among the undead, Palladio narrowed his three eyes.</p>
<p class=\"block_2\">Their appearance clearly set them apart from mediocrity. The only thing remaining was whether their abilities would match that impression or not.</p>
<p class=\"block_2\">Palladio: \u201cWhat are you capable of doing?\u201d</p>
<p class=\"block_2\">???: \u201cHm, that is right\u2026 First of all, how about I show you.\u201d</p>
<p class=\"block_2\">Saying thus, the white-haired woman standing before Palladio smiled, and held her hand up towards the sky. And then\u2015\u2015</p>
<p class=\"block_12\">\u25b3\u25bc\u25b3\u25bc\u25b3\u25bc\u25b3</p>
<p class=\"block_2\">???: \u201c\u2015\u2015Ana!!\u201d</p>
<p class=\"block_2\">When the three heads of the Three-Headed Blight Dragon, whose appearance had been anticipated, were severed in the sky above the city, its colossal black frame reduced to dust as it crashed down from above, Anastasia felt a sense of relief in her heart.</p>
<p class=\"block_2\">Although it had been anticipated, the fact that the opponent was a heavy hitter remained unchanged.</p>
<p class=\"block_2\">Even with appropriate preparations, there lingered the ever-present possibility of the enemy surpassing or outflanking them. Having avoided such a scenario, she felt the relief of a powerful foe having been thwarted.</p>
<p class=\"block_2\">However, the solace Anastasia felt was torn to pieces by the voice of Echidna at her neck.</p>
<p class=\"block_2\">Anastasia: \u201c\u2015\u2015\u2015\u2015\u201d</p>
<p class=\"block_2\">Having known each other for a decade, the Spirit Echidna usually remained motionless masquerading as Anastasia\u2019s scarf; bouncing up on her shoulder, she stared with black eyes up at the sky above the great fortress.</p>
<p class=\"block_2\">Tracing the gaze of Echidna, Anastasia\u2019s pale turquoise eyes widened.</p>
<p class=\"block_2\">Anastasia: \u201cIs that\u2026 a star\u2026?\u201d</p>
<p class=\"block_2\">Her murmured words rang uncertain, a manifestation of her lack of confidence.</p>
<p class=\"block_2\">At the very least, one could say that it was a sight Anastasia had never seen in her lifetime, a scenery she could have never even imagined.</p>
<p class=\"block_2\">Higher than the flock of undead flying dragons that crossed over Mount Gildray, higher than the Three-Headed Blight Dragon which had ascended even further beyond that, light was cascading down upon the city from above\u2015\u2015 a star was falling.</p>
<p class=\"block_2\">Next to Anastasia as she marveled at the extraordinary sight, as Otto and Berstetz were left speechless, Serena, witnessing the same scene, contorted the sword scar on her face into a smile,</p>
<p class=\"block_2\">Serena: \u201cThe atmosphere has changed\u2015\u2015 Win or lose, the conclusion draws near.\u201d</p>
<p class=\"block_12\">\u25b3\u25bc\u25b3\u25bc\u25b3\u25bc\u25b3</p>
<p class=\"block_2\">???: \u201cHaha, hahahaha! Excellent, yes, this is it! The sight I had coveted!\u201d</p>
<p class=\"block_2\">Witnessing the sight unfolding in the sky of the battlefield, Palladio broke into ecstatic dance.</p>
<p class=\"block_2\">The defenses of the Fortified City, known for their solidity, would amount to naught once the cascading light reached the ground. The resistance of those puny imbeciles would equate to rubbish before the star\u2019s radiance.</p>
<p class=\"block_2\">Palladio: \u201cYou have done well to appear before me! I shall enlist you among mine vassals! By what name shall I address you!?\u201d</p>
<p class=\"block_2\">Joy shimmering in his three golden eyes, Palladio posed the question to the white-haired woman who had given rise to that sight. Once again catching a frontward glimpse of the woman, who had turned to face him following his query, Palladio caught his breath.</p>
<p class=\"block_2\">Beautiful white hair and refined features capable of sending shivers down one\u2019s spine, but above all else, her face and eyes were bereft of the physical traits that could identify her as an undead\u2015\u2015 It was an appearance that could cause one to mistake her as a living being.</p>
<p class=\"block_2\">But then, why would she contribute to his side?</p>
<p class=\"block_2\">When Palladio questioned this, the woman deeply bent her hips, and bowed.</p>
<p class=\"block_2\">And then, she returned an answer to his question\u2015\u2015 An introduction as to just who exactly she was.</p>
<p class=\"block_2\">???: \u201cWhat name would be correct to use, is a bit of a complicated affair. So for the time being\u2026 I suppose you can just call me the Witch of Greed.\u201d</p>
<p class=\"block_2\">So she declared.</p>
</body>
```"""

# Tokenize and count tokens
tokens = encoding.encode(text)
token_count = len(tokens)

# Display results
print(f"Number of tokens: {token_count}")

messages = [
         {
            "role": "system", 
            "content": "Please translate the following text from English to German while maintaining the markdown of the html document, tone, style, and specific terminology that are characteristic of the Re: zero light novel series. Focus on preserving the emotional nuances of each character's dialogue and the detailed descriptions that contribute to the fantasy setting. Aim for a translation that reflects both the formal and casual language used in the series. Don't translate <!-- Source: {filename} -->. Don't add additional comments besides translation"
        }, {
            "role": "user", 
            "content": text,
        }
    ]

if input("Are you sure?") == 'y':
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o-mini",
    )

    try:
        response_message = chat_completion.choices[0].message.content
        with open('out.txt', 'w') as f:
            f.write(response_message)
        print(response_message)
    except:
        with open('chat_completion.pkl', 'wb') as file:
            pickle.dump(chat_completion, file)

