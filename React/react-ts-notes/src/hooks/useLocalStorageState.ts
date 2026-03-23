import { useEffect, useState } from 'react'

type UseLocalStorageStateOptions<T> = {
  serialize?: (value: T) => string
  deserialize?: (raw: string) => T
}

export function useLocalStorageState<T>(
  key: string,
  initialValue: T,
  options?: UseLocalStorageStateOptions<T>,
) {
  const serialize = options?.serialize ?? JSON.stringify
  const deserialize = options?.deserialize ?? (JSON.parse as (raw: string) => T)

  const [value, setValue] = useState<T>(() => {
    try {
      const raw = localStorage.getItem(key)
      return raw == null ? initialValue : deserialize(raw)
    } catch {
      return initialValue
    }
  })

  useEffect(() => {
    try {
      localStorage.setItem(key, serialize(value))
    } catch {
      // ignore write errors (private mode/quota)
    }
  }, [key, serialize, value])

  return [value, setValue] as const
}
