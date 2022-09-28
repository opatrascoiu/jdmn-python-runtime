#
# Copyright 2016 Goldman Sachs.
#
# Licensed under the Apache License, Version 2.0 (the "License") you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License at
#     http:#www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations under the License.
#
import isodate

from jdmn.feel.lib.Types import STRING, DURATION, DATE, LONG


class DefaultDurationLib:
    def duration(self, from_: STRING) -> DURATION:
        if from_ is None:
            return None

        return isodate.parse_duration(from_)

    def yearsAndMonthsDuration(self, from_: DATE, to: DATE) -> DURATION:
        if from_ is None or to is None:
            return None

        delta = to - from_
        return delta

    def years(self, duration: DURATION) -> LONG:
        if duration is None:
            return None

        return duration.years

    def months(self, duration: DURATION) -> LONG:
        if duration is None:
            return None

        return duration.months

    def days(self, duration: DURATION) -> LONG:
        if duration is None:
            return None

        return duration.days

    def hours(self, duration: DURATION) -> LONG:
        if duration is None:
            return None

        seconds = duration.seconds
        mm, ss = divmod(seconds, 60)
        hh, mm = divmod(mm, 60)
        return hh

    def minutes(self, duration: DURATION) -> LONG:
        if duration is None:
            return None

        seconds = duration.seconds
        mm, ss = divmod(seconds, 60)
        hh, mm = divmod(mm, 60)
        return mm

    def seconds(self, duration: DURATION) -> LONG:
        if duration is None:
            return None

        seconds = duration.seconds
        mm, ss = divmod(seconds, 60)
        return ss

    def abs(self, duration: DURATION) -> DURATION:
        if duration is None:
            return None

        return duration.years
