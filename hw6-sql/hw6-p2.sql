select title from album;
select album.title from album join artist on album.artist_id = artist.id where artist.name = "Tom Petty";
select track.title from album join track on album.id = track.album_id where album.title = "Revolver";
select distinct album.title from track join genre on track.genre_id = genre.id join album on track.album_id = album.id where genre.name = "Folk";