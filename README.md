# Colour Museum NFT Analysis

I recently came across the upcoming NFT marketplace _Color Museum_ (from hereon 'CM'), which aims to fundraise using the novel concept of allowing investors to mint 10,000 tokens that each represent a unique colour. Creators are then attracted to sell their NFTs on the marketplace by CM's commission rate of 1.25%, compared with 2.5% for OpenSea. This commission rate is then shared amongst creators based on the composition of the piece's colours. This concept interested me for a number of reasons, but mostly it stood out because unlike most NFT mints which are seemingly luck-of-the-draw in their returned value (based on rarity), there exists a way for an investor to generate alpha through wise selection.

> There exists a way for an investor to generate alpha through wise selection

In this exercise we'll be analysing a dataset of some of the most traded NFT art collections in order to deduce which colours should produce the highest return from future marketplace listings. This means making the following assumptions:

1. The CM marketplace will be used by NFT creators to sell their artwork
2. The colour palette used in NFTs over the past few years will be predictive of the colour palettes used in future pieces

Number 1 is out of our control, and of course I wouldn't be writing this if I already thought that was incorrect<sup>±</sup> . For assumption 2 we could test for stationarity across time, but due to an inaccessbility of release dates for projects across a large enough scale we'll opt to also assume this to be true in favour of using a wider dataset.

There are many ways we could go about assessing which colour of the dataset is the highest value:

* The colour(s) used in the highest individual value pieces
* The colour(s) with the highest aggregate value across pieces
* The colour(s) most commonly used across the entire data

One key mechanism of CM is that in lieu of someone owning a colour present, the owner with the closest colour by cosine distance will be awarded the respective commission. This introduces a final measure of profitability for a colour:

* The colour(s) with the broadest range of nearby colours by total composition

Of course this last one assumes that no one else owns other colours in the space, but that information won't be known until all 10,000 have been minted.



I originally intended to use the [entire dataset of NFTs provided via the NFT bay](https://thenftbay.org/description.html), but unfortunately I have neither the time nor space to process all 17 TB of images. I'm also not convinced this would provide a more reliable result, as at collections that made no money are essentially noise for the purposes of this investment thesis.



To find the centroid point we use [the median](https://stackoverflow.com/questions/77936/whats-the-best-way-to-calculate-a-3d-or-n-d-centroid)



± = My largest hunch for why Color Marketplace will at least see some volume traded on it is due to the successful pre-launch marketing they've ran, the community they've grown as well as the novel idea behind it. Like with all early stage projects (**espectially** in crypto) there is of course a great deal of uncertainty around this assumption, but only time will tell.