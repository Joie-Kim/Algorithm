function solution(genres, plays) {
  let answer = [];
  // 노래 리스트를 만든다.
  let songs = genres.map((genre, index) => {
    return {
      no: index,
      genre: genre,
      play: plays[index],
    };
  });

  // 장르별 재생수 리스트를 만든다.
  let playOfGenre = [];
  songs.forEach((song) => {
    let thisGenre = playOfGenre.find(
      (playGenre) => playGenre.genre === song.genre
    );
    if (!thisGenre) {
      playOfGenre.push({
        genre: song.genre,
        play: song.play,
      });
    } else {
      thisGenre.play += song.play;
    }
  });

  // 재생수를 기준으로 장르를 정렬한다. (내림차순)
  playOfGenre.sort((a, b) => b.play - a.play);

  // 재생수가 많은 장르의 노래들을 고르고, play를 기준으로 정렬한다. (내림차순)
  // 총 노래 수가 1개 이하면 1개만 고른다.
  playOfGenre.forEach((playGenre) => {
    let thisSongs = songs.filter((song) => song.genre === playGenre.genre);
    thisSongs.sort((a, b) => b.play - a.play);
    answer.push(thisSongs[0].no);
    if (thisSongs.length > 1) {
      answer.push(thisSongs[1].no);
    }
  });

  return answer;
}

console.log(
  solution(
    ["classic", "pop", "classic", "classic", "pop"],
    [500, 600, 150, 800, 2500]
  )
);
console.log(solution(["classic", "pop"], [500, 600]));
console.log(
  solution(
    ["A", "A", "B", "A", "B", "B", "A", "A", "A", "A"],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
  )
);
console.log(solution(["a", "b", "b", "c", "c"], [5, 5, 40, 5, 5]));
