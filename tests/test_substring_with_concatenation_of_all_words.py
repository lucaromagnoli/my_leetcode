import pytest
from other.substring_with_concatenation_of_all_words import Solution


@pytest.fixture
def solution():
    return Solution()


@pytest.mark.parametrize(
    "s, words, expected",
    [
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "good"], [8]),
        ("barfoothefoobarman", ["foo", "bar"], [0, 9]),  # Example 1
        ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),  # Example 2
        ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),  # Example 3
        ("", ["foo", "bar"], []),  # Empty string
        ("barfoothefoobarman", [], []),  # Empty words list
        ("barfoothefoobarman", ["foo"], [3, 9]),  # Single word in words list
        ("barfoo", ["bar", "foo", "the"], []),  # Words list longer than string
        ("barfoobar", ["bar", "foo"], [0, 3]),  # Overlapping substrings
    ],
)
def test_finds_correct_substring_indices(solution, s, words, expected):
    assert sorted(solution.findSubstring(s, words)) == sorted(expected)


@pytest.mark.parametrize(
    "s, words, expected",
    [
        (
            [
                "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel",
                [
                    "dhvf",
                    "sind",
                    "ffsl",
                    "yekr",
                    "zwzq",
                    "kpeo",
                    "cila",
                    "tfty",
                    "modg",
                    "ztjg",
                    "ybty",
                    "heqg",
                    "cpwo",
                    "gdcj",
                    "lnle",
                    "sefg",
                    "vimw",
                    "bxcb",
                ],
                [935],
            ]
        )
    ],
)
def test_large(solution, s, words, expected):
    assert sorted(solution.findSubstring(s, words)) == sorted(expected)
