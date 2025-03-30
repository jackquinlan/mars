import * as React from "react";

import { getBaseUrl } from "@/lib/utils";

export default async function Home() {
  let data = await fetch(`${getBaseUrl()}/api/chess/get-move`).then((res) =>
    res.json(),
  );

  return <div>{data.message}</div>;
}
