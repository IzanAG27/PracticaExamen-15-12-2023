def getAppleSongStanza(applesCount):
    if applesCount == 1:
        POMA = "poma"
    else:
        POMA = "pometes"

    stanza = f"\n{applesCount} {POMA} té el pomer,\n" \
             f"de {applesCount} una, de {applesCount} una,\n" \
             f"{applesCount} {POMA} té el pomer,\n" \
             f"de {applesCount} una en caigué.\n" \
             f"Si mireu el vent d'on vé\n" \
             f"veureu el pomer com dansa,\n" \
             f"si mireu el vent d'on vé\n" \
             f"veureu com dansa el pomer."
    return stanza


def recur_pomes(applesCount):
    if applesCount == 0:
        print("No hi ha pomes al pomer.")
    else:
        print(getAppleSongStanza(applesCount))
        return recur_pomes(applesCount - 1)


def main():
    recur_pomes(992)


if __name__ == "__main__":
    main()
