import json
from math import floor, pow, log

class DooTubeHelpers:
    """DooTube helpers class
    """

    def percent(self, current, total):
        """Percent function. Gets two values to return percentage of download process

        Args:
            current (int): Actual filesize downloaded
            total (int): Total filesize

        Returns:
            int: Percantage of file download
        """
        if current < 1:
            return 0
        perc = round((float(current) / float(total)) * float(100))
        return perc

    def streams_jsonify(self, streams):
        """Gets Youtube streams, and converts them to json file

        Args:
            streams (StreamQuery): Gets StreamQuery object from pytube

        Returns:
            dict: Json dictionary
        """
        dictArray = []
        stream_keys = ["itag", "mime_type", "res", "fps", "abr", "audio_codec", "filesize"]

        for x in stream_keys:
            stream_values = [x.itag, x.mime_type, x.resolution, x.fps, x.audio_codec, convert_to_size_type(x.filesize)]
            dictArray.append(dict(zip(stream_keys, stream_values)))

        return json.dumps(dictArray)

    def convert_to_size_type(self, bytes):
        """Converts to size type based on bytes input.

        Args:
            bytes (byte): Gets bytes filesize and converts it to more readable form.

        Returns:
            str: File size redable for human
        """
        if bytes == 0:
            return "0B"
        size_name = ("B", "Kb", "Mb", "Gb", "Tb")
        i = int(floor(log(bytes, 1024)))
        p = pow(1024, i)
        s = round(bytes / p, 2)
        return "%s %s" % (s, size_name[i])

